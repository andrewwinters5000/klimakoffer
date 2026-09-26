include("milestone1.jl")
include("milestone2.jl")
include("milestone3.jl")
include("milestone4.jl")
include("milestone5.jl")

using SparseArrays
using Random  # standard library

function timestep_euler_backward_2d(jacobian, delta_t)
    A = factorize(sparse(I - delta_t * jacobian))

    function timestep_function(temperature, t, delta_t,
                               mesh, diffusion_coeff, heat_capacity, solar_forcing,
                               radiative_cooling)
        if t == 1
            t_old = size(temperature, 3)
        else
            t_old = t - 1
        end
        # Similar to MS3, we have to solve the equation
        # T_t = T_{t-1} + delta_t * f(T_t, t),
        # where f(T, t) = R(T) + F(t).
        # We use the fact that R is linear and thus can be written as R(T) = AT, where A is the Jacobian of R.
        # Solving for T_t yields
        # T_t = (I - delta_t * A)^{-1} * (T_{t-1} + delta_t * F(t)).
        @views source_terms = calc_source_terms_ebm_2d(heat_capacity,
                                                       solar_forcing[:, :, t],
                                                       radiative_cooling)

        return @views temperature[:, :, t] = reshape(A \ vec(temperature[:, :, t_old] +
                                                         delta_t * source_terms),
                                                     (mesh.n_latitude, mesh.n_longitude))
    end

    return timestep_function
end

function co2_evolution(jacobian, mesh, diffusion_coeff, heat_capacity, solar_forcing)
    # Read CO2 data
    co2_data = readdlm(joinpath(@__DIR__, "input", "co2_nasa.dat"))

    # Assume that only data for full years is available
    n_years = Int(size(co2_data, 1) / 12)

    average_co2 = [sum(co2_data[(12y + 1):(12y + 12), 4]) / 12 for y in 0:(n_years - 1)]

    ntimesteps = size(solar_forcing, 3)

    average_temperatures = zeros(n_years)
    annual_temperatures = zeros(ntimesteps * n_years)

    timestep_function = timestep_euler_backward_2d(jacobian, 1 / ntimesteps)

    temperature_grid = 15 *
                       ones((mesh.n_latitude, mesh.n_longitude, size(solar_forcing, 3)))

    for y in 1:n_years
        radiative_cooling = calc_radiative_cooling_co2(average_co2[y])
        (temperature_grid,
         area_mean_temp) = compute_equilibrium_2d(timestep_function,
                                                  mesh, diffusion_coeff,
                                                  heat_capacity,
                                                  solar_forcing,
                                                  radiative_cooling,
                                                  rel_error=1.0e-2,
                                                  initial_temperature=temperature_grid)
        annual_temperatures[(ntimesteps * (y - 1) + 1):(ntimesteps * y)] = area_mean_temp
        average_temperatures[y] = sum(area_mean_temp) / ntimesteps
    end

    first_year = Int(co2_data[1, 1])
    last_year = Int(co2_data[end, 1])

    return annual_temperatures, average_temperatures, first_year, last_year
end

function plot_co2_evolution(jacobian, mesh, diffusion_coeff, heat_capacity, solar_forcing)
    (annual_temperatures, average_temperatures, first_year,
     last_year) = co2_evolution(jacobian, mesh, diffusion_coeff,
                                heat_capacity, solar_forcing)

    n_timesteps = length(annual_temperatures)

    average_temperatures_per_month = [average_temperatures[floor(Int,
                                                                                      (t - 1) / 48) + 1]
                                      for t in 1:n_timesteps]

    labels = first_year:10:last_year

    p = plot(average_temperatures_per_month, label="average temperature",
             xlims=(1, n_timesteps), xticks=(1:480:n_timesteps, labels),
             ylabel="surface temperature [°C]",
             title="Annual temperature with CO2 data from NASA")
    plot!(p, annual_temperatures, label="annual temperature")

    return p
end

function calc_co2_uncertainty(co2_data)
    # Column 8 of co2_nasa.dat (NOAA's co2_mm_mlo.txt format) is the
    # "uncertainty of the monthly mean"; column 4, already used by
    # `co2_evolution`, is the monthly average itself.
    #
    # Month-to-month measurement uncertainties are treated as independent, so
    # they combine in quadrature; averaging 12 months then divides the
    # combined standard deviation by 12 (the number of months averaged):
    #   sigma_year = sqrt(sum_{m=1}^{12} sigma_m^2) / 12
    #
    # NOAA flags interpolated/missing months with a negative uncertainty;
    # those are replaced by the mean of that year's valid entries before
    # combining, so a single missing month doesn't produce a bogus (or
    # negative) variance.
    monthly_unc = co2_data[:, 8]
    n_years = Int(size(co2_data, 1) / 12)

    annual_unc = zeros(n_years)
    for y in 0:(n_years - 1)
        year_unc = copy(monthly_unc[(12y + 1):(12y + 12)])
        valid = year_unc .>= 0
        if any(valid)
            year_unc[.!valid] .= sum(year_unc[valid]) / count(valid)
        else
            # No valid uncertainty at all for this year; fall back to the
            # overall dataset average as a rough placeholder.
            all_valid = monthly_unc[monthly_unc .>= 0]
            year_unc .= sum(all_valid) / length(all_valid)
        end

        annual_unc[y + 1] = sqrt(sum(year_unc .^ 2)) / 12
    end

    return annual_unc
end

function co2_evolution_ensemble(jacobian, mesh, diffusion_coeff, heat_capacity, solar_forcing;
                                n_samples=30, rel_error=1.0e-2, seed=0)
    # Monte Carlo propagation of the CO2 measurement uncertainty through the
    # 2D EBM. For each of `n_samples` ensemble members, every year's CO2
    # concentration is independently perturbed by a Gaussian draw with the
    # NOAA-reported uncertainty for that year, and the full multi-decade
    # `co2_evolution` simulation is rerun with the perturbed CO2 series.
    #
    # This reruns the whole equilibrium simulation n_samples times, so it is
    # the expensive but most general option. Because each year is iterated to
    # equilibrium (`compute_equilibrium_2d`), the result for a given year is
    # determined almost entirely by that year's own CO2 value (the previous
    # year's temperature field is only used as a warm-start initial guess),
    # so relaxing `rel_error` for the ensemble members is usually safe and
    # speeds things up considerably.
    Random.seed!(seed)

    co2_data = readdlm(joinpath(@__DIR__, "input", "co2_nasa.dat"))
    n_years = Int(size(co2_data, 1) / 12)

    average_co2 = [sum(co2_data[(12y + 1):(12y + 12), 4]) / 12 for y in 0:(n_years - 1)]
    co2_sigma = calc_co2_uncertainty(co2_data)

    ntimesteps = size(solar_forcing, 3)
    timestep_function = timestep_euler_backward_2d(jacobian, 1 / ntimesteps)

    average_temperatures_ensemble = zeros(n_samples, n_years)

    for s in 1:n_samples
        # CO2 concentrations cannot be negative or unreasonably small; clip
        # defensively in case of an unusually wide sigma or a bad draw.
        co2_sample = max.(average_co2 .+ co2_sigma .* randn(n_years), 1.0)

        temperature_grid = 15 * ones((mesh.n_latitude, mesh.n_longitude, ntimesteps))
        for y in 1:n_years
            radiative_cooling = calc_radiative_cooling_co2(co2_sample[y])
            (temperature_grid,
             area_mean_temp) = compute_equilibrium_2d(timestep_function, mesh,
                                                      diffusion_coeff, heat_capacity,
                                                      solar_forcing, radiative_cooling,
                                                      rel_error=rel_error,
                                                      initial_temperature=temperature_grid,
                                                      verbose=false)
            average_temperatures_ensemble[s, y] = sum(area_mean_temp) / ntimesteps
        end

        println("Ensemble member $s/$n_samples done.")
    end

    first_year = Int(co2_data[1, 1])
    last_year = Int(co2_data[end, 1])

    return average_temperatures_ensemble, first_year, last_year
end

function plot_co2_evolution_with_uncertainty(jacobian, mesh, diffusion_coeff, heat_capacity,
                                             solar_forcing; n_samples=30)
    (ensemble, first_year,
     last_year) = co2_evolution_ensemble(jacobian, mesh, diffusion_coeff, heat_capacity,
                                        solar_forcing, n_samples=n_samples)

    n_years = size(ensemble, 2)
    mean_temperature = [sum(ensemble[:, y]) / n_samples for y in 1:n_years]
    std_temperature = [sqrt(sum((ensemble[:, y] .- mean_temperature[y]) .^ 2) / n_samples)
                       for y in 1:n_years]

    years = first_year:(first_year + n_years - 1)

    p = plot(years, mean_temperature, ribbon=std_temperature, fillalpha=0.3,
             label="mean annual-average temperature (±1σ)",
             xlabel="year", ylabel="surface temperature [°C]",
             title="Annual-mean temperature with CO2 uncertainty propagated ($n_samples samples)")

    return p
end

function co2_instance_ensemble(co2_ppm, co2_sigma, jacobian, mesh, diffusion_coeff,
                               heat_capacity, solar_forcing; n_samples=50, seed=0)
    # Propagate the uncertainty of a single CO2 measurement (e.g.
    # co2_ppm = 422.99, co2_sigma = 0.42) into the equilibrium annual
    # temperature cycle, separately for north, south and total area-mean
    # temperature.
    #
    # Unlike `co2_evolution_ensemble`, this is a single CO2 value (one year,
    # one instant), not a multi-decade series - so there is no year-to-year
    # chain to warm-start from. We still warm-start each draw from the
    # previous one, since consecutive samples are close together (both near
    # co2_ppm), which speeds up convergence of `compute_equilibrium_2d`
    # considerably.
    #
    # The Jacobian only depends on the diffusion coefficients and the linear
    # radiative feedback B, not on CO2 itself (which enters only as the
    # additive source term `radiative_cooling`), so the same `jacobian` can be
    # reused for every ensemble member without recomputation.
    Random.seed!(seed)

    ntimesteps = size(solar_forcing, 3)
    timestep_function = timestep_euler_backward_2d(jacobian, 1 / ntimesteps)

    co2_samples = max.(co2_ppm .+ co2_sigma .* randn(n_samples), 1.0)

    north_ensemble = zeros(n_samples, ntimesteps)
    south_ensemble = zeros(n_samples, ntimesteps)
    total_ensemble = zeros(n_samples, ntimesteps)

    temperature = zeros((mesh.n_latitude, mesh.n_longitude, ntimesteps))
    for s in 1:n_samples
        radiative_cooling = calc_radiative_cooling_co2(co2_samples[s])
        (temperature, _) = compute_equilibrium_2d(timestep_function, mesh, diffusion_coeff,
                                                  heat_capacity, solar_forcing,
                                                  radiative_cooling,
                                                  initial_temperature=temperature,
                                                  verbose=false)

        north_ensemble[s, :] = [calc_mean_north(temperature[:, :, t], mesh.area)
                                for t in 1:ntimesteps]
        south_ensemble[s, :] = [calc_mean_south(temperature[:, :, t], mesh.area)
                                for t in 1:ntimesteps]
        total_ensemble[s, :] = [calc_mean(temperature[:, :, t], mesh.area)
                                for t in 1:ntimesteps]

        println("Ensemble member $s/$n_samples done (CO2 = $(round(co2_samples[s], digits=4)) ppm).")
    end

    return north_ensemble, south_ensemble, total_ensemble, co2_samples
end

function plot_annual_temperature_north_south_with_uncertainty(north_ensemble, south_ensemble,
                                                               total_ensemble, co2_ppm,
                                                               co2_sigma)
    # Like `plot_annual_temperature_north_south` (MS4), but for an ensemble of
    # annual temperature cycles (from `co2_instance_ensemble`), plotting the
    # ensemble mean for north/south/total together with a ±1σ band from the
    # underlying CO2 uncertainty (via Plots.jl's `ribbon` keyword).
    #
    # Note: CO2's influence on temperature is weak, so for a small co2_sigma
    # the resulting band can be only a fraction of a degree wide - i.e. easy
    # to miss at a glance, not a sign that the propagation did nothing.
    n_samples, ntimesteps = size(total_ensemble)
    labels = ["March", "June", "September", "December", "March"]

    mean_total = [sum(total_ensemble[:, t]) / n_samples for t in 1:ntimesteps]
    mean_north = [sum(north_ensemble[:, t]) / n_samples for t in 1:ntimesteps]
    mean_south = [sum(south_ensemble[:, t]) / n_samples for t in 1:ntimesteps]

    std_total = [sqrt(sum((total_ensemble[:, t] .- mean_total[t]) .^ 2) / n_samples)
                for t in 1:ntimesteps]
    std_north = [sqrt(sum((north_ensemble[:, t] .- mean_north[t]) .^ 2) / n_samples)
                for t in 1:ntimesteps]
    std_south = [sqrt(sum((south_ensemble[:, t] .- mean_south[t]) .^ 2) / n_samples)
                for t in 1:ntimesteps]

    avg_total = sum(mean_total) / ntimesteps
    avg_north = sum(mean_north) / ntimesteps
    avg_south = sum(mean_south) / ntimesteps

    p = plot(mean_total, ribbon=std_total, fillalpha=0.25, label="temperature (total)",
             xlims=(1, ntimesteps), xticks=(LinRange(1, ntimesteps, 5), labels),
             ylabel="surface temperature [°C]",
             title="Annual temperature with CO2 = $co2_ppm ± $co2_sigma [ppm]")
    plot!(p, avg_total * ones(ntimesteps), label="average temperature (total)", linestyle=:dash)
    plot!(p, mean_north, ribbon=std_north, fillalpha=0.25, label="temperature (north)")
    plot!(p, avg_north * ones(ntimesteps), label="average temperature (north)", linestyle=:dash)
    plot!(p, mean_south, ribbon=std_south, fillalpha=0.25, label="temperature (south)")
    plot!(p, avg_south * ones(ntimesteps), label="average temperature (south)", linestyle=:dash)

    return p
end

function co2_instance_sensitivity(co2_ppm, co2_sigma, jacobian, mesh, diffusion_coeff,
                                  heat_capacity, solar_forcing; delta_co2=1.0)
    # Deterministic alternative to `co2_instance_ensemble`: instead of Monte
    # Carlo sampling, estimate d(temperature)/d(CO2) via a central finite
    # difference around co2_ppm, then propagate the uncertainty analytically
    # as sigma_T = |dT/dCO2| * co2_sigma. This has no sampling noise and needs
    # only 3 model runs (regardless of how small co2_sigma is), which is
    # appropriate here since co2_sigma/co2_ppm is tiny enough that the
    # model's response is essentially linear over that range - there's no
    # curvature for Monte Carlo to usefully explore.
    #
    # delta_co2 sets the finite-difference step (in ppm); it should be small
    # compared to co2_ppm but large enough to avoid floating-point
    # cancellation - a few ppm is a safe default here, well inside the linear
    # regime.
    ntimesteps = size(solar_forcing, 3)
    timestep_function = timestep_euler_backward_2d(jacobian, 1 / ntimesteps)

    function run(co2)
        radiative_cooling = calc_radiative_cooling_co2(co2)
        (temperature, _) = compute_equilibrium_2d(timestep_function, mesh, diffusion_coeff,
                                                  heat_capacity, solar_forcing,
                                                  radiative_cooling, verbose=false)
        north = [calc_mean_north(temperature[:, :, t], mesh.area) for t in 1:ntimesteps]
        south = [calc_mean_south(temperature[:, :, t], mesh.area) for t in 1:ntimesteps]
        total = [calc_mean(temperature[:, :, t], mesh.area) for t in 1:ntimesteps]
        return north, south, total
    end

    (north_minus, south_minus, total_minus) = run(co2_ppm - delta_co2)
    (north_mean, south_mean, total_mean) = run(co2_ppm)
    (north_plus, south_plus, total_plus) = run(co2_ppm + delta_co2)

    sigma_north = abs.(north_plus .- north_minus) ./ (2 * delta_co2) .* co2_sigma
    sigma_south = abs.(south_plus .- south_minus) ./ (2 * delta_co2) .* co2_sigma
    sigma_total = abs.(total_plus .- total_minus) ./ (2 * delta_co2) .* co2_sigma

    return (north_mean, sigma_north), (south_mean, sigma_south), (total_mean, sigma_total)
end

function plot_annual_temperature_north_south_with_sigma(north, south, total, co2_ppm, co2_sigma)
    (mean_north, sigma_north) = north
    (mean_south, sigma_south) = south
    (mean_total, sigma_total) = total

    ntimesteps = length(mean_total)
    labels = ["March", "June", "September", "December", "March"]

    avg_total = sum(mean_total) / ntimesteps
    avg_north = sum(mean_north) / ntimesteps
    avg_south = sum(mean_south) / ntimesteps

    p = plot(mean_total, ribbon=sigma_total, fillalpha=0.25, label="temperature (total)",
             xlims=(1, ntimesteps), xticks=(LinRange(1, ntimesteps, 5), labels),
             ylabel="surface temperature [°C]",
             title="Annual temperature with CO2 = $co2_ppm ± $co2_sigma [ppm] (finite-difference σ)")
    plot!(p, avg_total * ones(ntimesteps), label="average temperature (total)", linestyle=:dash)
    plot!(p, mean_north, ribbon=sigma_north, fillalpha=0.25, label="temperature (north)")
    plot!(p, avg_north * ones(ntimesteps), label="average temperature (north)", linestyle=:dash)
    plot!(p, mean_south, ribbon=sigma_south, fillalpha=0.25, label="temperature (south)")
    plot!(p, avg_south * ones(ntimesteps), label="average temperature (south)", linestyle=:dash)

    return p
end

# Run code
function milestone6_uncertain()
    geo_dat = read_geography(joinpath(@__DIR__, "input", "The_World65x128.dat"))
    mesh = Mesh(geo_dat)

    albedo = calc_albedo(geo_dat)
    heat_capacity = calc_heat_capacity(geo_dat)

    # Compute solar forcing
    true_longitude = read_true_longitude(joinpath(@__DIR__, "input", "True_Longitude.dat"))
    solar_forcing = calc_solar_forcing(albedo, true_longitude)
    ntimesteps = length(true_longitude)

    # Compute and plot diffusion coefficient
    diffusion_coeff = calc_diffusion_coefficients(geo_dat)

    jacobian = calc_jacobian_ebm_2d(mesh, diffusion_coeff, heat_capacity)

    # Ensemble propagation of the CO2 measurement uncertainty through the
    # multi-decade NASA CO2 evolution (expensive: reruns the full equilibrium
    # simulation n_samples times - lower n_samples for a quicker check).
    plot_co2_evolution_uncertainty = plot_co2_evolution_with_uncertainty(jacobian, mesh,
                                                                        diffusion_coeff,
                                                                        heat_capacity,
                                                                        solar_forcing,
                                                                        n_samples=30)

    # Single-instance CO2 uncertainty: propagate one measurement (e.g. the
    # current CO2 = 422.99 ± 0.44 ppm) into the north/south/total annual
    # temperature cycle, via Monte Carlo ...
    co2_ppm_instance, co2_sigma_instance = 422.99, 0.44
    (north_ens, south_ens,
     total_ens, _) = co2_instance_ensemble(co2_ppm_instance, co2_sigma_instance, jacobian,
                                          mesh, diffusion_coeff, heat_capacity, solar_forcing,
                                          n_samples=50)
    plot_instance_ensemble = plot_annual_temperature_north_south_with_uncertainty(north_ens,
                                                                                  south_ens,
                                                                                  total_ens,
                                                                                  co2_ppm_instance,
                                                                                  co2_sigma_instance)

    # ... and via the cheap finite-difference sensitivity, for comparison.
    (north_fd, south_fd,
     total_fd) = co2_instance_sensitivity(co2_ppm_instance, co2_sigma_instance, jacobian, mesh,
                                         diffusion_coeff, heat_capacity, solar_forcing)
    plot_instance_sensitivity = plot_annual_temperature_north_south_with_sigma(north_fd, south_fd,
                                                                               total_fd,
                                                                               co2_ppm_instance,
                                                                               co2_sigma_instance)

    # Show the plots
    display(plot_co2_evolution_uncertainty)
    display(plot_instance_ensemble)
    display(plot_instance_sensitivity)

    return plot_co2_evolution_uncertainty, plot_instance_ensemble, plot_instance_sensitivity
end
