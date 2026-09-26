import os

import numpy as np
from matplotlib import pyplot as plt
from scipy import sparse

from milestone1 import read_geography
from milestone2 import calc_albedo, calc_heat_capacity, calc_solar_forcing, read_true_longitude
from milestone3 import calc_radiative_cooling_co2, calc_mean, plot_annual_temperature
from milestone4 import plot_annual_temperature_north_south, calc_mean_north, calc_mean_south, plot_temperature
from milestone5 import calc_diffusion_coefficients, calc_source_terms_ebm_2d, Mesh, compute_equilibrium_2d, \
    calc_jacobian_ebm_2d


def timestep_euler_backward_2d(jacobian, delta_t_):
    m, n = jacobian.shape
    eye = sparse.eye(m, n, format="csc")
    jacobian = sparse.csc_matrix(jacobian)
    solve = sparse.linalg.factorized(eye - delta_t_ * jacobian)

    def timestep_function(temperature, t, delta_t,
                          mesh, _, heat_capacity, solar_forcing, radiative_cooling):
        # Similar to MS3, we have to solve the equation
        # T_t = T_{t-1} + delta_t * f(T_t, t),
        # where f(T, t) = R(T) + F(t).
        # We use the fact that R is linear and thus can be written as R(T) = AT, where A is the Jacobian of R.
        # Solving for T_t yields
        # T_t = (I - delta_t * A)^{-1} * (T_{t-1} + delta_t * F(t)).
        source_terms = calc_source_terms_ebm_2d(heat_capacity, solar_forcing[:, :, t], radiative_cooling)

        temperature[:, :, t] = np.reshape(solve((temperature[:, :, t - 1] + delta_t * source_terms).flatten()),
                                          (mesh.n_latitude, mesh.n_longitude))

    return timestep_function


def calc_co2_uncertainty(co2_data):
    """
    Aggregate the NOAA per-month uncertainty of the monthly CO2 mean (column 7,
    "unc. of mon mean" in co2_mm_mlo.txt / co2_nasa.dat) into a per-year
    uncertainty of the annual-average CO2 concentration used by `co2_evolution`.

    Assumes month-to-month measurement uncertainties are independent, so they
    combine in quadrature; averaging 12 months then divides the combined
    standard deviation by 12 (the number of months averaged):

        sigma_year = sqrt(sum_{m=1}^{12} sigma_m^2) / 12

    NOAA flags interpolated/missing months with a negative uncertainty; those
    are replaced by the mean of that year's valid uncertainties before
    combining, so a single missing month doesn't produce a bogus (or negative)
    variance.
    """
    monthly_unc = co2_data[:, 7].copy()
    n_years = int(co2_data.shape[0] / 12)

    annual_unc = np.zeros(n_years)
    for y in range(n_years):
        year_unc = monthly_unc[12 * y:12 * (y + 1)].copy()
        valid = year_unc >= 0
        if valid.any():
            year_unc[~valid] = np.mean(year_unc[valid])
        else:
            # No valid uncertainty reported for this year at all; fall back to
            # the overall dataset average as a rough placeholder.
            year_unc[:] = np.mean(monthly_unc[monthly_unc >= 0])

        annual_unc[y] = np.sqrt(np.sum(year_unc ** 2)) / 12

    return annual_unc


def analytic_temperature_uncertainty(average_co2, co2_sigma, radiative_cooling_feedback=2.15):
    """
    Cheap analytic approximation to the yearly-average temperature uncertainty.
    Valid for the *global* area-mean temperature only (see module docstring
    discussion): since the discretized diffusion operator conserves energy
    (its area-weighted mean is ~0), the equilibrium area-mean temperature
    satisfies T_avg = (S_avg - A) / B exactly, where A = radiative_cooling and
    B = radiative_cooling_feedback. Because
    A = radiative_cooling_base - 5.35 * log(CO2 / CO2_base), this gives the
    closed form

        sigma_T_avg = 5.35 / (B * CO2) * sigma_CO2

    Use this as a fast sanity check against `co2_evolution_ensemble` below,
    not as a replacement for it - it's worth confirming the conservation
    assumption numerically (e.g. checking that calc_mean of the diffusion
    operator at equilibrium is close to 0) before trusting it blindly.
    """
    return 5.35 / (radiative_cooling_feedback * average_co2) * co2_sigma


def co2_instance_sensitivity(co2_ppm, co2_sigma, jacobian, mesh, diffusion_coeff, heat_capacity, solar_forcing,
                             delta_co2=1.0, co2_concentration_base=315.0, radiative_cooling_base=210.3):
    """
    Deterministic alternative to `co2_instance_ensemble`: instead of Monte Carlo
    sampling, estimate d(temperature)/d(CO2) via a central finite difference
    around co2_ppm, then propagate the uncertainty analytically as
    sigma_T = |dT/dCO2| * co2_sigma. This has no sampling noise and needs only
    2 model runs (regardless of how small co2_sigma is), which is appropriate
    here since co2_sigma/co2_ppm is tiny enough that the model's response is
    essentially linear over that range - there's no curvature for Monte Carlo
    to usefully explore.

    delta_co2 sets the finite-difference step (in ppm); it should be small
    compared to co2_ppm but large enough to avoid floating-point cancellation
    - a few ppm is a safe default here, well inside the linear regime.

    Returns mean and sigma arrays (shape (ntimesteps,)) for north, south, total.
    """
    ntimesteps = solar_forcing.shape[2]
    timestep_function = timestep_euler_backward_2d(jacobian, 1 / ntimesteps)

    def run(co2):
        radiative_cooling = calc_radiative_cooling_co2(co2, co2_concentration_base=co2_concentration_base,
                                                        radiative_cooling_base=radiative_cooling_base)
        temperature, _ = compute_equilibrium_2d(timestep_function, mesh, diffusion_coeff, heat_capacity,
                                                 solar_forcing, radiative_cooling, verbose=False)
        north = np.array([calc_mean_north(temperature[:, :, t], mesh.area) for t in range(ntimesteps)])
        south = np.array([calc_mean_south(temperature[:, :, t], mesh.area) for t in range(ntimesteps)])
        total = np.array([calc_mean(temperature[:, :, t], mesh.area) for t in range(ntimesteps)])
        return north, south, total

    north_minus, south_minus, total_minus = run(co2_ppm - delta_co2)
    north_mean, south_mean, total_mean = run(co2_ppm)
    north_plus, south_plus, total_plus = run(co2_ppm + delta_co2)

    sigma_north = np.abs(north_plus - north_minus) / (2 * delta_co2) * co2_sigma
    sigma_south = np.abs(south_plus - south_minus) / (2 * delta_co2) * co2_sigma
    sigma_total = np.abs(total_plus - total_minus) / (2 * delta_co2) * co2_sigma

    return (north_mean, sigma_north), (south_mean, sigma_south), (total_mean, sigma_total)


def plot_annual_temperature_north_south_with_sigma(north, south, total, co2_ppm, co2_sigma):
    (mean_north, sigma_north), (mean_south, sigma_south), (mean_total, sigma_total) = north, south, total
    ntimesteps = len(mean_total)
    t = np.arange(ntimesteps)

    fig, ax = plt.subplots()
    for mean_t, sigma_t, label, color in [
        (mean_total, sigma_total, "total", "C0"),
        (mean_north, sigma_north, "north", "C1"),
        (mean_south, sigma_south, "south", "C2"),
    ]:
        avg_t = np.sum(mean_t) / ntimesteps
        ax.plot(t, avg_t * np.ones(ntimesteps), linestyle="--", color=color, alpha=0.6,
               label=f"average temperature ({label})")
        ax.plot(t, mean_t, color=color, label=f"temperature ({label})")
        print(f"Measured standard deviation due to CO2 (for {label}): {np.max(sigma_t)}")
        ax.fill_between(t, mean_t - sigma_t, mean_t + sigma_t, color=color, alpha=0.25)

    ax.set_xlim((0, ntimesteps - 1))
    ax.set_xticks(np.linspace(0, ntimesteps - 1, 5))
    ax.set_xticklabels(["March", "June", "September", "December", "March"])
    ax.set_ylabel("surface temperature [°C]")
    ax.grid()
    ax.set_title(f"Annual temperature with CO2 = {co2_ppm} ± {co2_sigma} [ppm] (finite-difference σ)")
    ax.legend(loc="upper right", fontsize="small")
    plt.tight_layout()
    plt.show()


def co2_evolution_ensemble(jacobian, mesh, diffusion_coeff, heat_capacity, solar_forcing,
                           n_samples=30, seed=0, rel_error=1e-2):
    """
    Monte Carlo propagation of the CO2 measurement uncertainty through the 2D
    EBM. For each of `n_samples` ensemble members, every year's CO2
    concentration is independently perturbed by a Gaussian draw with the
    NOAA-reported uncertainty for that year (from `calc_co2_uncertainty`), and
    the full multi-decade `co2_evolution` simulation is rerun with the
    perturbed CO2 series.

    Returns the ensemble of yearly-average global-mean temperatures, shape
    (n_samples, n_years), plus the first/last year of the data (for plotting).

    Note: this reruns the whole equilibrium simulation n_samples times, so it
    is the expensive but most general option. Because each year is iterated
    to equilibrium (`compute_equilibrium_2d`), the result for a given year is
    determined almost entirely by that year's own CO2 value (the previous
    year's temperature field is only used as a warm-start initial guess), so
    relaxing `rel_error` slightly for the ensemble members is usually safe and
    speeds things up considerably. Reduce `n_samples` if this is too slow on
    your machine; a few dozen is normally enough to see a stable ±1σ band.
    """
    co2_data = np.genfromtxt("input/co2_nasa.dat")
    n_years = int(co2_data.shape[0] / 12)

    average_co2 = np.array(
        [np.sum(co2_data[12 * y:12 * (y + 1), 3]) / 12 for y in range(n_years)]
    )
    co2_sigma = calc_co2_uncertainty(co2_data)

    ntimesteps = solar_forcing.shape[2]
    timestep_function = timestep_euler_backward_2d(jacobian, 1 / ntimesteps)

    rng = np.random.default_rng(seed)
    average_temperatures_ensemble = np.zeros((n_samples, n_years))

    for s in range(n_samples):
        co2_sample = rng.normal(average_co2, co2_sigma)
        # CO2 concentrations cannot be negative or unreasonably small;
        # clip defensively in case of an unusually wide sigma or bad draw.
        co2_sample = np.clip(co2_sample, 1.0, None)

        temperature = np.zeros((mesh.n_latitude, mesh.n_longitude, ntimesteps))
        for y in range(n_years):
            radiative_cooling = calc_radiative_cooling_co2(co2_sample[y])
            temperature, area_mean_temp = compute_equilibrium_2d(
                timestep_function, mesh, diffusion_coeff, heat_capacity, solar_forcing,
                radiative_cooling, initial_temperature=temperature,
                rel_error=rel_error, verbose=False)
            average_temperatures_ensemble[s, y] = np.sum(area_mean_temp) / ntimesteps

        print(f"Ensemble member {s + 1}/{n_samples} done.")

    first_year = int(co2_data[0, 0])
    last_year = int(co2_data[-1, 0])

    return average_temperatures_ensemble, first_year, last_year


def plot_co2_evolution_with_uncertainty(jacobian, mesh, diffusion_coeff, heat_capacity, solar_forcing,
                                        n_samples=30):
    """
    Like `plot_co2_evolution`, but propagates the CO2 measurement uncertainty
    through the simulation via `co2_evolution_ensemble` and plots the
    resulting mean yearly-average temperature with a ±1σ confidence band.
    """
    ensemble, first_year, last_year = co2_evolution_ensemble(
        jacobian, mesh, diffusion_coeff, heat_capacity, solar_forcing, n_samples=n_samples)

    mean_temperature = ensemble.mean(axis=0)
    std_temperature = ensemble.std(axis=0)
    years = np.arange(first_year, first_year + len(mean_temperature))

    fig, ax = plt.subplots()
    ax.plot(years, mean_temperature, color="C0", label="mean annual-average temperature")
    ax.fill_between(years, mean_temperature - std_temperature, mean_temperature + std_temperature,
                    color="C0", alpha=0.3, label="±1σ from CO2 uncertainty")

    ax.set_xlabel("year")
    ax.set_ylabel("surface temperature [°C]")
    ax.grid()
    ax.set_title(f"Annual-mean temperature with CO2 uncertainty propagated ({n_samples} samples)")
    ax.legend(loc="upper left")

    plt.tight_layout()
    plt.show()

    return mean_temperature, std_temperature, years


def co2_instance_ensemble(co2_ppm, co2_sigma, jacobian, mesh, diffusion_coeff, heat_capacity, solar_forcing,
                          n_samples=100, seed=0, co2_concentration_base=315.0, radiative_cooling_base=210.3):
    """
    Propagate the uncertainty of a single CO2 measurement (e.g. co2_ppm = 422.99,
    co2_sigma = 0.42) into the equilibrium annual temperature cycle, separately
    for the north, south and total area-mean temperature.

    Unlike `co2_evolution_ensemble`, this is a single CO2 value (one year, one
    instant), not a multi-decade series - so there is no year-to-year chain to
    warm-start from. We still warm-start each draw from the previous one, since
    consecutive samples are close together (both near co2_ppm), which speeds up
    convergence of `compute_equilibrium_2d` considerably.

    The Jacobian only depends on the diffusion coefficients and the linear
    radiative feedback B, not on CO2 itself (which enters only as the source
    term `radiative_cooling`), so the same `jacobian` can be reused for every
    ensemble member without recomputation.

    Returns three arrays of shape (n_samples, ntimesteps) - the north, south
    and total area-mean annual temperature cycle for each Monte Carlo draw -
    plus the array of sampled CO2 values.
    """
    ntimesteps = solar_forcing.shape[2]
    timestep_function = timestep_euler_backward_2d(jacobian, 1 / ntimesteps)

    rng = np.random.default_rng(seed)
    co2_samples = rng.normal(co2_ppm, co2_sigma, size=n_samples)
    co2_samples = np.clip(co2_samples, 1.0, None)

    north_ensemble = np.zeros((n_samples, ntimesteps))
    south_ensemble = np.zeros((n_samples, ntimesteps))
    total_ensemble = np.zeros((n_samples, ntimesteps))

    temperature = None
    for s, co2 in enumerate(co2_samples):
        radiative_cooling = calc_radiative_cooling_co2(co2, co2_concentration_base=co2_concentration_base,
                                                        radiative_cooling_base=radiative_cooling_base)
        temperature, _ = compute_equilibrium_2d(timestep_function, mesh, diffusion_coeff, heat_capacity,
                                                 solar_forcing, radiative_cooling,
                                                 initial_temperature=temperature, verbose=False)

        north_ensemble[s] = [calc_mean_north(temperature[:, :, t], mesh.area) for t in range(ntimesteps)]
        south_ensemble[s] = [calc_mean_south(temperature[:, :, t], mesh.area) for t in range(ntimesteps)]
        total_ensemble[s] = [calc_mean(temperature[:, :, t], mesh.area) for t in range(ntimesteps)]

        print(f"Ensemble member {s + 1}/{n_samples} done (CO2 = {co2:.4f} ppm).")

    return north_ensemble, south_ensemble, total_ensemble, co2_samples


def plot_annual_temperature_north_south_with_uncertainty(north_ensemble, south_ensemble, total_ensemble,
                                                         co2_ppm, co2_sigma):
    """
    Like `plot_annual_temperature_north_south` (MS4), but for an ensemble of
    annual temperature cycles (from `co2_instance_ensemble`), plotting the
    ensemble mean for north/south/total together with a ±1σ band from the
    underlying CO2 uncertainty.

    Note: CO2's influence on temperature is weak, so for a small co2_sigma the
    resulting band can be only a fraction of a degree wide - i.e. easy to miss
    at a glance, not a sign that the propagation did nothing.
    """
    ntimesteps = total_ensemble.shape[1]
    t = np.arange(ntimesteps)

    fig, ax = plt.subplots()

    for ensemble, label, color in [
        (total_ensemble, "total", "C0"),
        (north_ensemble, "north", "C1"),
        (south_ensemble, "south", "C2"),
    ]:
        mean_t = ensemble.mean(axis=0)
        std_t = ensemble.std(axis=0)
        print("Measured standard deviation due to CO2 (from n =",len(ensemble),"):",np.max(std_t))
        avg_t = np.sum(mean_t) / ntimesteps

        ax.plot(t, avg_t * np.ones(ntimesteps), linestyle="--", color=color, alpha=0.6,
               label=f"average temperature ({label})")
        ax.plot(t, mean_t, color=color, label=f"temperature ({label})")
        # Multiply by 10 to (artificially) make the band more visible
        ax.fill_between(t, mean_t - 10*std_t, mean_t + 10*std_t, color=color, alpha=0.25)

    ax.set_xlim((0, ntimesteps - 1))
    labels = ["March", "June", "September", "December", "March"]
    ax.set_xticks(np.linspace(0, ntimesteps - 1, 5))
    ax.set_xticklabels(labels)
    ax.set_ylabel("surface temperature [°C]")
    ax.grid()
    ax.set_title(f"Annual temperature with CO2 = {co2_ppm} ± {co2_sigma} [ppm]")
    ax.legend(loc="upper right", fontsize="small")

    plt.tight_layout()
    plt.show()


# Run code
if __name__ == '__main__':
    geo_dat_ = read_geography("input/The_World65x128.dat")
    mesh_ = Mesh(geo_dat_)

    albedo_ = calc_albedo(geo_dat_)
    heat_capacity_ = calc_heat_capacity(geo_dat_)

    # Compute solar forcing
    true_longitude_ = read_true_longitude("input/True_Longitude.dat")
    solar_forcing_ = calc_solar_forcing(albedo_, true_longitude_)
    ntimesteps_ = len(true_longitude_)

    diffusion_coeff_ = calc_diffusion_coefficients(geo_dat_)

    jacobian_ = calc_jacobian_ebm_2d(mesh_, diffusion_coeff_, heat_capacity_)

    # Propagate the CO2 measurement uncertainty into the simulated temperature.
    # This reruns the full multi-decade equilibrium simulation n_samples times,
    # so it is noticeably slower than the deterministic run above - low

    # plot_co2_evolution_with_uncertainty(jacobian_, mesh_, diffusion_coeff_, heat_capacity_, solar_forcing_,
    #                                     n_samples=3)

    # # Single-instance CO2 uncertainty: propagate one measurement (e.g. the
    # # current CO2 = 422.99 ± 0.44 ppm), which is August 2024 from the file,
    # # into the north/south/total annual temperature cycle.
    # # Reuses jacobian_ since it doesn't depend on CO2.
    # # NOTE: This is a brute force Monte Carlo approach that converges very slowly
    # co2_ppm_instance, co2_sigma_instance = 422.99, 0.44
    # expected_uncertainty = analytic_temperature_uncertainty(co2_ppm_instance, co2_sigma_instance)
    # print("Expected standard deviation due to CO2:", expected_uncertainty)
    # north_ens, south_ens, total_ens, _ = co2_instance_ensemble(
    #     co2_ppm_instance, co2_sigma_instance, jacobian_, mesh_, diffusion_coeff_, heat_capacity_, solar_forcing_,
    #     n_samples=50)
    # plot_annual_temperature_north_south_with_uncertainty(north_ens, south_ens, total_ens,
    #                                                      co2_ppm_instance, co2_sigma_instance)

    # Instead, because the CO2 sensitivity is so weak, it can be done in a smarter way.
    # Determine influence of one measurement (e.g. the
    # current CO2 = 422.99 ± 0.44 ppm), which is August 2024 from the file,
    # into the north/south/total annual temperature cycle.
    # The sensitivity is (essentially) linear as 0.44 / 422.99 ≈ 0.1%
    # Reuses jacobian_ since it doesn't depend on CO2.
    co2_ppm_instance, co2_sigma_instance = 422.99, 0.44
    expected_uncertainty = analytic_temperature_uncertainty(co2_ppm_instance, co2_sigma_instance)
    print("Expected standard deviation due to CO2:", expected_uncertainty)

    north_fd, south_fd, total_fd = co2_instance_sensitivity(
    co2_ppm_instance, co2_sigma_instance, jacobian_, mesh_, diffusion_coeff_, heat_capacity_, solar_forcing_)
    plot_annual_temperature_north_south_with_sigma(north_fd, south_fd, total_fd, co2_ppm_instance, co2_sigma_instance)
