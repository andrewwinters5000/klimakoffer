+++
title = "Milestone 6.5"
hascode = false
rss = "Description"
rss_title = "Milestone 6.5"
rss_pubdate = Date(2026, 9, 24)

tags = ["climatesystem"]
+++

# Milestone 6.5 - Introduction

In mathematical models and numerical methods errors are unavoidable.
For instance, the simple act of saving numbers on a computer and evaluating expressions
with them can accumulate round-off errors.
We are always aware of this in scientific computing and, in the worst case, these round-off
errors can accumulate and lead to unreliable results.
This is the concept of **conditioning** discussed in any entry level numerical analysis course.
It allows us to analyze a given problem, like the inversion of a matrix, and quantify how "reliable" a numerical solution can be when considering small changes in the inputs.
There, one learns that a stable numerical algorithm, like $LU$ with row pivoting, can still
fail if a matrix is ill-conditioned.

Beyond finite precision, other common sources of error are in the mathematical modeling
steps that arise from underlying assumptions as well as measurement errors in quantities used
within the mathematical model itself.
Recall, in the EBM we made many modeling assumptions like in the design of the outgoing radiation model $S_{OLW}(T,x,t)$ in [milestone 2](/milestone2/milestone2_radiation)
or in the choice of particular parameters within the final model like the albedo values
within the heat capacity $C(x)$.

A natural question is how do these errors in modeling or parameters influence the solution?
This question has lead to an entire field of study known as **Uncertainty Quantification** (UQ).
A main goal of this field of study is to understand and interpret how the uncertainty of parameters propagate through a model and affect the resulting solution.
Said solution is then equipped with appropriate confidence intervals (or some kind of error bar estimation) to inform practitioners on its reliability.

The uncertainty can be expressed in many ways, and it has a direct influence on the sophistication of the UQ methodology.
Importantly, one should consider how the uncertain parameters may be correlated to one another.
Or one may need to acknowledge some amount of correlation between the physical parameters and the spatial discretization strategy, as this potentially blends together modeling errors, measurement errors, and approximation errors.
Obviously, these correlations can be quite complex and difficult to exactly quantify.
Therefore, there are many tools available to researchers to study how functional correlated uncertainty
behaves, like [`uncertainties`](https://uncertainties.readthedocs.io/en/latest/) in python or [Measurements.jl](https://arxiv.org/pdf/1610.08716) in Julia.

The simplest strategy to quantify uncertainty is in terms of the standard deviation $\sigma$, which means that some quantity of interest $c$ in given by $c \pm \sigma$.
As a first example, consider the linear advection of some solution $u(x,t)$
$$
\frac{\partial u}{\partial t} + a \frac{\partial u}{\partial x} = 0,
$$
with $a>0$ and the initial condition $u(x,0) = u_0(x)$.
The exact solution is known to be the translated initial condition $u(x,t) = u_0(x - at)$ for all space and time.
However, suppose that the wave velocity $a$ was uncertain, how does this influence the solution reliability?
Below we show a numerical experiment where the initial condition is a sine wave and the wave velocity is uncertain with $a = 1.0 \pm 0.1$.
The propagation of uncertainty is done with the Julia package [Measurements.jl](https://github.com/juliaphysics/measurements.jl) that employs the [linear error propagation theory](https://en.wikipedia.org/wiki/Propagation_of_uncertainty#Linear_combinations).
The result of a simulation up to final time $1.5$ is given below.

\fig{/assets/milestone6p5/advection_error_bar.png}
* Uncertainty propagation in the linear advection equation with uncertain velocity. Source: [Trixi.jl](https://trixi-framework.org/TrixiDocumentation/stable/tutorials/differentiable_programming/#Propagating-errors-using-Measurements.jl).

The mean value solution is the solid blue line plotted against the errors bars. We see that the extrema, as expected, are less prone to uncertainty compared to the intermediate values, where the local variation is largest near the turning points of the sine wave.

## A first foray into EBM uncertainty

Turning focus towards the EBM, there are many places where uncertainty has been introduced.
One of the simplest entry points is in the outgoing radiation model $S_{OLW}(T,x,t)$ which
took the form
$$
S_{OLW}(T,x,t) = A(CO_2) + BT.
$$
with $B = 2.15\,\,[W/m^2/K]$ and
$$
A(CO_2) = 210.3 - 5.35\,\ln\left(\frac{CO_2}{C_{ref}}\right)\,\,[W/m^2],
$$
where throughout the milestones we took the value $C_{ref} = 315\,[ppm]$ is the reference concentration of carbon dioxide in the year $t_0=1950$.
However, the reference value $C_{ref}$ changes with the year.
For instance, we have access to data taken by [NASA at the Mauna Loa Observatory in Hawaii](https://gml.noaa.gov/ccgg/trends/mlo.html) for the $CO_2$ concentration in the atmosphere.
This data provides monthly values for the mean $CO_2$ concentration together with the data uncertainty.
For instance, in August 2024 the $CO_2$ concentration is given by $422.99 \pm 0.44\, [ppm]$.
Immediately, we see that the uncertainty is quite small compared to the mean value (approximately $0.01\%$).
So, one expects that making small changes in the $CO_2$ concentration would have a relatively small impact on the resulting solution of the EBM solution.

To estimate this influence of uncertainty in the $C_{ref}$ value may have, we differentiate $A(CO_2)$
with respect to this variable to see
$$
\frac{d}{dC_{ref}}A(CO_2) = \frac{5.35}{C_{ref}}.
$$
From this, we estimate the uncertainty in the value of $A(CO_2)$ to be proportional to the uncertainty in $C_{ref}$ as
$$
\sigma_A \approx \frac{d}{dC_{ref}}A(CO_2)\sigma_C = \frac{5.35}{C_{ref}}\sigma_C
$$
Substituting the values $C_{ref} = 422.99$ and $\sigma_C = 0.44$ we have that $\sigma_A \approx 0.005565$.
So, the relative importance of the uncertainty and variation in the $CO_2$ concentration is very weak
in the EBM considered in this course.
That is, small changes in the $CO_2$ concentration will cause a minimal (if at all noticeable effect) in the predicted surface temperature.

@@colbox-blue
**Remark:** There is further uncertainty present in the radiation model in the additional
coefficients in $A(CO_2)$ as well as $B$. One could further explore the influence of the
$CO_2$ concentration of the surface termperature by changing to a different model than
that of [Budyko in milestone 2](https://andrewwinters5000.github.io/klimakoffer/milestone2/milestone2_radiation/#budykos_empirical_infrared_model).
For instance, looking at the observation data something other than a linear model may capture
the trend in the data better.
The uncertainty associated with this new curve fitting could then be evaluated and compared
against the previously used Budyko model.
@@


There are many other parameter quantities in the EBM and some may have a stronger influence on the numerical solution, like the albedo or the diffusion coefficient.
However, making an estimate like that above using the chain rule becomes increasing difficult.
This is due to the interior coupling of the multitude of model parameters where the compound effect of the uncertainties (whether correlated or linked through some other lurking variable) become impossible to quantify analytically.
For instance, try to imagine finding this partial derivative with respect to a component of the diffusion coefficent written in spherical coordinates.
It does not seem fruitful.
Also, this chain rule estimation technique discounts any correlation effects between model components, so there is a futher limitation.
Instead, we turn to other methods that attempt to quantify this complex interaction of model parameters and uncertainties.