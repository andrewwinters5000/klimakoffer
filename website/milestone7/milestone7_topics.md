+++
title = "Milestone 7"
hascode = false
rss = "Description"
rss_title = "Milestone 7"
rss_pubdate = Date(2026, 9, 1)

tags = ["climatesystem"]
+++

# Milestone 7 - Possible topics

\toc

Below we list different topics that could be investigated for milestone 7.
If your group wants to propose an alternative or modified topic, this is okay, just contact us to discuss the new projecr area.

## Parameter sensitivity and uncertainty

The EBM contains a number of physical and empirical parameters, including the surface albedo, heat-transport diffusivity, and parameters describing the radiative forcing from atmospheric CO2.

Perform a systematic parameter study in which one or more model parameters are varied over physically reasonable ranges. Initially consider one parameter at a time, and subsequently investigate interactions between parameters. Determine how the parameters affect quantities such as the global mean temperature, seasonal temperature variation, polar amplification, and the spatial distribution of temperature.

Use the results to identify which parameters the model is most sensitive to. Compare local sensitivity measures, such as derivatives or finite differences, with global sensitivity measures based on the full parameter ensemble.

In a second stage, assign probability distributions to uncertain model parameters and perform a Monte Carlo uncertainty-quantification study. Generate an ensemble of model simulations and use the resulting distributions to estimate quantities such as confidence intervals for global mean temperature and regional temperature.
<!-- Sobol sensitivity indices or Latin hypercube sampling -->

Finally, investigate which uncertain parameters contribute most strongly to the uncertainty in the predicted climate. Discuss the implications for interpreting predictions from simplified climate models.

References:
- Ziegler, E., & Rehfeld, K. (2021). TransEBM v. 1.0: description, tuning, and validation of a transient model of the Earth's energy balance in two dimensions. Geoscientific Model Development, 14(5), 2843-2866. [GMD](https://gmd.copernicus.org/articles/14/2843/2021/)

- North, G. R., Cahalan, R. F., & Coakley Jr, J. A. (1981). Energy balance climate models. Reviews of Geophysics, 19(1), 91-121. doi: [10.1029/RG019i001p00091](https://doi.org/10.1029/RG019i001p00091)


<!-- There are several parameters in the EBM such as albedo, diffusivity, or CO2 forcing.
Perturb these parameters in a systematic way (either individually or together) and perform many simulations.
Analyze the average climate behavior and identify which parameters have the largest impact on the results.
From this parameter study, perform Monte Carlo simulations to quantify the uncertainty in model predictions and estimate confidence intervals. -->

## Stochastic forcing

The deterministic EBM predicts the response of the climate system to a prescribed forcing. In reality, the climate system is continually perturbed by unresolved and unpredictable processes occurring on shorter timescales.

Introduce stochastic forcing into the EBM by adding a random component to the energy-balance equation. Investigate different types of forcing, including white noise and temporally correlated noise with characteristic timescales ranging from short weather-like fluctuations to longer climate variability.

Perform ensembles of simulations for each choice of noise amplitude and correlation timescale. Analyze the resulting probability distributions, temporal autocorrelation, variance, and power spectra of global and regional temperature.

Investigate how the climate system filters the imposed stochastic forcing. In particular, determine whether short-timescale forcing produces primarily short-term temperature fluctuations or whether it can generate variability on substantially longer timescales.

Compare the stochastic simulations with the corresponding deterministic solution and investigate how many independent realizations are required to obtain reliable estimates of climate statistics.

References:
- Hasselmann, K. (1976). Stochastic climate models part I. Theory. Tellus, 28(6), 473-485. doi: [10.1111/j.2153-3490.1976.tb00696.x]( https://doi.org/10.1111/j.2153-3490.1976.tb00696.x)
- North, G. R., Cahalan, R. F., & Coakley Jr, J. A. (1981). Energy balance climate models. Reviews of Geophysics, 19(1), 91-121. doi: [10.1029/RG019i001p00091](https://doi.org/10.1029/RG019i001p00091)

## Physics-Informed Neural Networks (PINNs)
<!-- Possibly too much work -->

Solve the EBM using a physics-informed neural network rather than a conventional numerical discretization.

Construct a neural network representation of the temperature field and train it by minimizing a loss function based on the residual of the governing energy-balance equation. Incorporate the appropriate spatial and temporal boundary conditions into the training procedure.

Validate the PINN solution against the reference solution produced by the existing Klimakoffer implementation. Compare the two approaches in terms of accuracy, computational cost, convergence behavior, and sensitivity to numerical and training parameters.

Investigate the influence of the neural-network architecture, number and distribution of collocation points, optimization strategy, and relative weighting of different components of the loss function.

Finally, discuss whether a PINN offers any practical advantages for this particular problem. Consider both its ability to solve the governing equations and its potential to incorporate additional information or constraints that would be difficult to include in a conventional numerical method.

References:
- Waqas, M., & Kim, S. M. (2026). Physics-informed neural networks and variants in weather and hydrological modeling: a systematic review. Natural Hazards Research. doi: [10.1016/j.nhres.2026.07.003](https://doi.org/10.1016/j.nhres.2026.07.003)

## Neural network surrogate model
<!-- Possibly too much work; can use TensorFlow or Flux.jl -->

A numerical climate model may be inexpensive to run once but computationally expensive when thousands or millions of simulations are required. A neural network can potentially be trained to reproduce the behavior of the climate model at a fraction of the computational cost.

Generate a large ensemble of EBM simulations covering a range of CO2 concentrations, orbital parameters, surface properties, and other relevant model inputs. Use these simulations as training data for a neural-network surrogate.

Train the network to predict quantities such as the global mean temperature, seasonal temperature distribution, or complete spatial temperature field. Compare different network architectures and investigate how the amount and distribution of training data affects the surrogate's accuracy.

Evaluate the surrogate on parameter combinations that were not included in the training set. Pay particular attention to extrapolation and to whether errors are concentrated in particular geographic regions or climate regimes.

Finally, compare the computational cost of the original EBM with that of the trained surrogate. Estimate the number of simulations required before the surrogate becomes computationally advantageous.

References:
- Fuchs, D., Sherwood, S. C., Prasad, A., & Lue, N. (2026). The Benefits of Lateral Connections: Toward a Stable Neural Network Surrogate for Climate Model Parameterization. Artificial Intelligence for the Earth Systems, 5(3), 250115. doi: [10.1175/AIES-D-25-0115.1](https://doi.org/10.1175/AIES-D-25-0115.1)

## Catastrophe scenarios

Use the EBM to investigate the climatic response to extreme climate perturbations of the Earth's radiative and surface properties. The objective is not to produce a detailed prediction of a real catastrophe, but to investigate how simplified climate models respond to large changes in radiative forcing and surface characteristics.

For each scenario, identify the physical processes that need to be represented in the EBM and determine which assumptions of the original model remain valid. Modify the appropriate model parameters or source terms and investigate both the transient response and the eventual equilibrium state.

Compare the magnitude and timescale of the response between different scenarios and identify the feedback mechanisms responsible for the simulated changes.

- **Complete Ice Melt**: Remove the permanent ice and snow cover from the model and recompute the equilibrium climate. Quantify the resulting change in global and regional temperature and investigate the role of the ice–albedo feedback. Compare the result with simulations in which the ice cover is allowed to respond dynamically to temperature.
- **Volcanic Winter**: Model a major volcanic eruption by introducing a temporary reduction in incoming solar radiation representing stratospheric aerosol loading. Investigate the magnitude and duration of the resulting cooling and the spatial distribution of the response. Explore how the response depends on the magnitude, spatial distribution, and lifetime of the aerosol perturbation.
- **Asteroid Impact**: Model the climatic consequences of a large asteroid impact by introducing a temporary reduction in incoming solar radiation representing atmospheric dust and aerosol loading. Investigate the magnitude and duration of the resulting "impact winter" and determine which assumptions about aerosol lifetime and radiative forcing have the greatest influence on the result. Compare the simulated climate response with published estimates for the climatic consequences of the Chicxulub impact. Discuss which processes cannot be represented by the EBM and therefore limit the interpretation of the results.

References:
- Kaiho, K., & Oshima, N. (2025). The significance of impact-induced hydrocarbon soot aerosols in global climate change and extinctions. Palaeogeography, Palaeoclimatology, Palaeoecology, 113237. doi: [10.1016/j.palaeo.2025.113237](https://doi.org/10.1016/j.palaeo.2025.113237)
- Morgan, J. V., Bralower, T. J., Brugger, J., & Wünnemann, K. (2022). The Chicxulub impact and its environmental consequences. Nature Reviews Earth & Environment, 3(5), 338-354. doi: [10.1038/s43017-022-00283-y](https://doi.org/10.1038/s43017-022-00283-y)
- North, G. R., Cahalan, R. F., & Coakley Jr, J. A. (1981). Energy balance climate models. Reviews of Geophysics, 19(1), 91-121. doi: [10.1029/RG019i001p00091](https://doi.org/10.1029/RG019i001p00091)

## Nonlinear model with Newton iteration

The baseline EBM in Klimakoffer contains several processes that can be represented using linear or prescribed parameterizations. Introduce one or more nonlinear physical processes into the model, resulting in a nonlinear system of equations for the equilibrium temperature field.

Possible extensions include a temperature-dependent albedo representing the ice–albedo feedback, nonlinear outgoing longwave radiation, or other temperature-dependent parameterizations.

Develop a Newton or quasi-Newton solver for the resulting nonlinear system. Derive the Jacobian analytically where possible and compare this with finite-difference or approximate Jacobians.

Investigate the convergence of the nonlinear solver for different initial guesses and physical parameters. Compare the computational cost and convergence behavior with the original linear solver.

In particular, investigate whether the nonlinear model admits multiple equilibrium states. If multiple solutions exist, determine how the initial condition and model parameters influence which equilibrium is reached.

Discuss the implications of nonlinear feedbacks for climate sensitivity and the interpretation of equilibrium solutions.

References:
- Deblonde, G., Peltier, W. R., & Hyde, W. T. (1992). Simulations of continental ice sheet growth over the last glacial-interglacial cycle: experiments with a one level seasonal energy balance model including seasonal ice albedo feedback. Global and planetary change, 6(1), 37-55. doi: [10.1016/0031-0182(92)90255-4](https://doi.org/10.1016/0031-0182(92)90255-4)
- North, G. R., Cahalan, R. F., & Coakley Jr, J. A. (1981). Energy balance climate models. Reviews of Geophysics, 19(1), 91-121. doi: [10.1029/RG019i001p00091](https://doi.org/10.1029/RG019i001p00091)

## Spatially varying climate parameters

The baseline EBM uses spatially prescribed properties of the Earth's surface and atmosphere. Investigate how spatial heterogeneity in these properties affects the simulated climate.

Begin by introducing spatially varying surface albedo while keeping the heat-transport coefficient constant. For instance, the albedo term could have the form

Investigate the effects of continents, oceans, ice, and other surface types on the global temperature distribution.
$$
(1 - \alpha(x))S(x)
$$
where, as before, $x$ here is used for compactness to represent the latitutde and longitude coordinates.
Be aware that sharp transitions in the albedo when transitioning to ice may require particular attention.

Study how spatial resolution influences the representation of sharp transitions in albedo and diffusivity. Determine whether the resulting climate predictions converge as the spatial grid is refined.