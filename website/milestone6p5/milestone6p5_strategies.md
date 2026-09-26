+++
title = "Milestone 6.5"
hascode = false
rss = "Description"
rss_title = "Milestone 6.5"
rss_pubdate = Date(2026, 9, 24)

tags = ["ebm", "uncertainty"]
+++

# Milestone 6.5 - UQ strategies
Once uncertainty is introduced as an important quantity that we want to track
there are many, well-studied methodologies available to quantify its behavior.
Herein, we collect some of the most popular strategies but this is by no means
an exhaustive list.

## Polynomial chaos
This strategy involves expanding each of the uncertain quantities with a polynomial basis
to attempt and capture its behavior and influence.
Obviously, this can become very expensive as the number of uncertain variables grows as each feature has its
own polynomial expansion, e.g., the mean, variance, kurtosis, etc. as the features we wish to model.
For instance, in a fluid flow simulation one of the unknown quantities is the density $\rho$.
If we consider one spatial dimension with polynomial chaos then the density has a (truncated) stochastic expansion
where the random function has space and time dependence
$$
\rho v(x, t, \xi) = \sum_{k=1}^K\rho(x,t) \Psi_k(\xi)
$$
where $\Psi_k(\xi)$ is some set of basis functions in the stochastic solution space.
Therefore, these polynomial chaos methods can suffer an accelerated version of the *curse of dimensionality*.
In a sense, the 1D spatial problem becomes two dimensional and a 2D spatial problem become four dimensional due to the requirement of a stochastic variable in each direction.

Also, there is a huge amount of flexibility in the choice of basis functions, $\Psi_k(\xi)$, for this polynomial expansion in stochastic space.
Two common choices are Legendre polynomials or Haar wavelets, but many others are available.
There is also some interplay with numerical errors due to the numerical method (like a finite volume or a spectral method) together with the numerical approximation error introduces by the truncated polynomial expansion in stochastic space.
These methods can be very high-order both in approximation and stochastic space but with a high computational cost.

## Monte Carlo

One of the simplest, and maybe one could say "brute force", strategies to study uncertainty is the Monte Carlo family of methods.
The basic idea is that we know one (or more) parameters in the model contains uncertainty.
Thus, we run many, many simulations for slightly perturbed values of said parameters and then create an average solution over all the runs.
This is often called an **ensemble solution** for a particular problem for a given parameter space.
How one selects the perturbed values of each simulation can be guided by simple or complex assumptions.
The simplest strategy is to assume a normal distribution of the parameter of interest and create a large, random body of samples of this quantity according to this distribution.
For instance, if we have a single quantity to study with standard deviation uncertainty $\mu \pm \sigma$ then the Monte Carlo approach assumes $\mathcal{N}(\mu, \sigma^2)$ and random samples are taken as such.
How one samples this set of random numbers influences the quality and convergence of the sampling procedure to an (unknown) mean behavior.
Therefore, Monte Carlo is a powerful, albeit brute force, technique to study the uncertainty in approximations.

@@colbox-blue
**Remark:** Monte Carlo is quite slow in terms of convergence with respect ot its representative statistics, i.e., on the order of $\mathcal{O}(1/\sqrt{n})$ for the number of samples $n$.
This is because standard Monte Carlo uses random samples that may lead to unintended clustering in stochastic space.
Sobol sampling of the random variable space offers better convergence properties, on the order $\mathcal{O}(1/n)$, than the standard random sampling for such studies because it is a quasi-random low-discrepancy method that fills space more uniformly and provides deterministic reproducibility.
@@

### A Monte Carlo example regarding $A(CO_2)$
We apply the standard Monte Carlo technique to the EBM where we **only** modify the reference value
of the $CO_2$ concentration in the radiation term $A(CO_2)$ with $422.99 \pm 0.44\, [ppm]$.
Thus, we assume the value of the $CO_2$ concentration follow a normal distribution with $\mathcal{N}(422.99, 0.44^2)$ and we randomly sample this space of values.
We run 50 simulations with these random values to create our ensemble and give the surface temperature profiles below.

\fig{/assets/milestone6p5/result.png}
* Result of the 2D EBM with $C_{ref} = 422.99$ and uncertainty $\sigma_C = 0.44$ for 50 simulations with normally distributed values $C \sim \mathcal{N}(422.99, 0.44^2)$.

From a first visual inspection this plot looks identical to results from [milestone 6](/milestone6/milestone6_results). However, if we zoom into the lines we see that there is an uncertainty band in the surface temperature

\fig{/assets/milestone6p5/result_zoom.png}
* Zoom-in of solution for the result of the 2D EBM to show the $95\%$ confidence bars around the mean solution value.

These results reinforce our expectation from the analysis in the previous part of this lecture that the uncertainty in the $CO_2$ concentration plays an insignificant role in the overall EBM climate model.

## Bayesian inference
The strategies above all start from an *assumed* distribution for the uncertain parameter (e.g. the $\mathcal{N}(422.99, 0.44^2)$ we assumed for $CO_2$) and propagate it forward through the model.
Bayesian inference flips this strategy around.
Rather than assuming a distribution and propagating it forward, we use historic or observed data to work *backward* to a distribution over the model's parameters in the first place.
This is particularly useful for parameters that are not directly measured (like the diffusion coefficients in our EBM, which were tuned by hand rather than observed), where we would otherwise have no obvious way to assign an uncertainty at all.

The formal machinery is Bayes' theorem. If $\theta$ denotes a (possibly vector-valued) set of uncertain model parameters and $\mathcal{D}$ denotes observed data, then
$$
p(\theta \mid \mathcal{D}) = \frac{p(\mathcal{D}\mid \theta)\,p(\theta)}{p(\mathcal{D})}.
$$
Each term has a concrete interpretation for us:
- $p(\theta)$, the **prior**, encodes what we believe about the parameter before looking at any data - e.g. that a diffusion coefficient should be positive and within some physically sensible range.
- $p(\mathcal{D}\mid\theta)$, the **likelihood**, measures how well the EBM's output, run with a particular choice of $\theta$, agrees with the observed data $\mathcal{D}$ (for instance, how closely the simulated surface temperature climatology matches [ERA5 reanalysis](https://www.ecmwf.int/en/forecasts/dataset/ecmwf-reanalysis-v5) data).
- $p(\theta\mid\mathcal{D})$, the **posterior**, is the resulting updated distribution over the parameter, combining what we assumed beforehand with what the data actually tells us.
- $p(\mathcal{D})$ is a normalizing constant and is usually the hardest term to compute directly, which is precisely why we turn to sampling-based methods rather than evaluating this formula outright.

### Markov Chain Monte Carlo (MCMC)
In all but the simplest problems, the posterior $p(\theta\mid\mathcal{D})$ has no closed form that can written down and evaluate directly.
MCMC methods sidestep this by constructing a random walk through parameter space whose long-run distribution of visited points *is* the posterior, without ever needing to know the normalizing constant $p(\mathcal{D})$.
The most common variant, Metropolis-Hastings, works roughly as follows:
1. Start from some initial guess $\theta_0$ for the parameters.
2. Propose a new candidate $\theta'$, typically a small random perturbation of the current value.
3. Run the EBM forward with $\theta'$ and compute how much better (or worse) it matches the data than the current $\theta$, via the ratio of their (prior $\times$ likelihood) values.
4. Accept the move to $\theta'$ with a probability given by that ratio; otherwise stay at the current $\theta$.
5. Repeat for many thousands of steps, discarding an initial "burn-in" period before the chain has settled into the high-probability region of parameter space.

The resulting chain of accepted parameter values is a set of samples *from the posterior* - and, notably, this is already an ensemble in the same sense as the Monte Carlo section above, except the samples are concentrated where the model actually agrees with observed data, rather than spread according to an assumed prior distribution alone.

@@colbox-blue
**Remark:** Each step of the chain requires a full forward run of the model to evaluate the likelihood, exactly like standard Monte Carlo. For our 2D EBM, running the diffusive equilibrium solve thousands of times for a single MCMC calibration is expensive - one of the main motivations, together with the "many, many samples" issue from ordinary Monte Carlo. For the surrogate-model approach discussed next, a *cheap* ANN surrogate can stand in for the full model inside the MCMC loop, at the cost of introducing (and needing to validate) its own approximation error into the calibration.
@@

### An example: calibrating the diffusion coefficients
Concretely, one could treat the diffusion coefficients (`coeff_ocean_poles`, `coeff_ocean_equator`, `coeff_equator`, `coeff_north_pole`, `coeff_south_pole` in `calc_diffusion_coefficients`) as the uncertain parameter vector $\theta$, rather than the fixed, hand-tuned constants used throughout this course.
Using ERA5 reanalysis surface temperature climatology as the observed data $\mathcal{D}$, an MCMC run would explore the space of diffusion coefficients, favoring choices that make the EBM's simulated meridional temperature profile track the reanalysis data closely.
The result is not a single "best" set of diffusion coefficients, but a full posterior distribution over them - directly telling us, for instance, how tightly constrained the polar diffusion coefficient is by the available data compared to the equatorial one, and letting that calibrated uncertainty propagate into any later simulation via the same Monte Carlo machinery from before.

## Surrogate models (ANNs)
Turning up this idea from Bayesian inference to a logical extreme, as mathematicians like to do, we might arrive at surrogate models.
In essence, surrogate models are built from the requirement that we have a lot of outcome data from a process, but may not know (or may not want to re-derive) the mechanism that created it.
As strange as it sounds, this situation is quite common in computational science and engineering.
These surrogate models serve to replace design decisions and completely eschew the design of approximate models (as we have done in this course).

A modern approach for the creation of such surrogate models are artificial neural networks (ANNs).
These big data strategies help remove ambiguity in the "training" of the model.
An ANN surrogate is, at its core, a sophisticated curve-fitting device: an input layer, one or more hidden layers with a nonlinear activation function, and an output layer, whose weights are tuned (via gradient-based optimization and automatic differentiation) to minimize the mismatch between the network's prediction and a set of known input/output pairs.

### Why this helps with UQ
Recall from the previous discussion that Monte Carlo needs *many, many* evaluations of the model to converge its statistics at the (slow) rate $\mathcal{O}(1/\sqrt{n})$.
For our 2D EBM, a single equilibrium solve is expensive; a Monte Carlo study with hundreds or thousands of samples compounds that cost directly.
An ANN surrogate breaks this trade-off by moving the expense up front: we pay for a modest number of *true* EBM solves once, use them to train a cheap function approximator, and then run the (nearly free) surrogate as many times as we like.

\fig{/assets/milestone6p5/ann_surrogate_workflow.png}
* The surrogate modeling workflow: a design of experiments over the uncertain parameters (e.g. Latin hypercube or Sobol sampling of $CO_2$, diffusion coefficients, albedo parameters, etc.) generates training pairs from the full EBM; an ANN is trained on these pairs to approximate the map from parameters to a quantity of interest (e.g. annual-mean temperature); the trained network then stands in for the EBM in a large Monte Carlo ensemble.

Concretely, for our 2D EBM this could mean training a network to map $(CO_2, D, \alpha) \mapsto \overline{T}$, the equilibrium global-mean surface temperature, using perhaps a few hundred full 2D EBM solves as training data. Once trained, evaluating the surrogate for a new parameter draw costs a single forward pass through the network - orders of magnitude cheaper than a fresh equilibrium solve - which makes it feasible to run the tens of thousands of samples needed for, say, a reliable estimate of a 95% confidence interval, or a global sensitivity analysis (e.g. Sobol indices) across several uncertain parameters at once.

@@colbox-blue
**Caveats:** A surrogate is only as good as its training data. It must be validated against held-out (i.e. not used for training) full-model runs, and extrapolating a trained surrogate outside the region of parameter space it was trained on is unreliable - the network has no awareness of the underlying physics and will happily produce a smooth, confident-looking, and wrong answer outside its training envelope. This trade-off (upfront training cost and validation burden, in exchange for near-free repeated evaluation) is the central design decision in any surrogate modeling strategy.
@@

@@colbox-blue
**Remark:** Strategies built from ANNs firmly leave the idea of "first principles" modeling and are driven by available data and existing model results. There is currently a strong research push to enhance/generate parametrizations and even full sub-models/components
of GCMs/ESMs that are data-driven. Because the use of ANNs and surrogate models boil down to curve fitting (essentially), a grain of salt shouold be taken when assessing the validity of these models. It is possible that these models might over fit their parameters to existing observational data, which would diminish the predictive power of the models for scenarios they are not trained in.
@@

## Physics Informed Neural Networks (PINNs)
The next level of abstraction in parameter study is Physics Informed Neural Networks (PINNs) [(Raissi, Perdikaris & Karniadakis, 2019)](https://doi.org/10.1016/j.jcp.2018.10.045).
This strategy couples the big data aspects of surrogate models to a particular problem like our EBM.
Unlike the ANN surrogate above, which is trained purely on input/output *data* pairs from the full model, a PINN is trained to satisfy the governing equation itself.
The network represents the solution field directly: it takes the independent variables (space $x$, time $t$) and, crucially for UQ purposes, the uncertain parameters (e.g. $CO_2$) as inputs, and outputs an approximation $\hat{T}(x, t, CO_2)$ of the temperature field.
Because the uncertain parameter is fed in as an *input* rather than fixed at training time, a single trained network can be evaluated for any new parameter draw in a Monte Carlo ensemble without ever re-solving the underlying PDE - the parametric dependence on uncertainty is learned once, up front.

\fig{/assets/milestone6p5/pinn_training_loop.png}
* The PINN training loop for the EBM. The network's own output is checked against the model's governing equation (via automatic differentiation, rather than a numerical discretization), against the initial/boundary constraints, and optionally against any sparse observational data available; these residuals combine into a single loss whose gradient is backpropagated into the network weights.

Concretely, the total loss driving training is a weighted sum of several residual terms, evaluated at randomly sampled "collocation" points in the space-time-parameter domain:
- **PDE residual**: using automatic differentiation to compute $\partial T/\partial t$ and the diffusion operator directly from the network's own output, then penalizing any nonzero mismatch when substituted into the EBM's governing equation,
$$
C(x) \partialderiv{T}{t} + A(CO_2) + B T - \Nabla \cdot (D\Nabla T) = S_{sol}(x,t).
$$
- **Initial/boundary residual**: penalizing deviation from the prescribed initial temperature field and any boundary or periodicity constraints.
- **Data residual (optional)**: if sparse, possibly noisy observational data is available (e.g. historical station temperatures), an additional term nudges the network toward matching those observations - offering a natural bridge to the Bayesian ideas above.

@@colbox-blue
**Remark:** In climate modeling the boundary conditions are a nonissue, as the Earth climate system is treated as periodic. However, much work is done in improving or quantifying the initial conditions for the climate system. For instance, at Sveriges meteorologiska och hydrologiska institut (SMHI) they  use big-data tools to anchor simulations in real-world states for near-term forecasting and ensemble variability.
@@

Over successive optimization steps (e.g. Adam followed by L-BFGS), the network's weights are updated to jointly minimize all of these residuals at once, so that the trained network is simultaneously a good curve fit to any available data *and* an approximate solution of the PDE.
This comes at the cost of significant upfront computational overhead in training, with the tradeoff being that the particular discretization of the EBM becomes irrelevant once training is complete - the network is a mesh-free, continuous representation of the solution that can be queried anywhere in space, time, or parameter space.
However, because the PINN strategy uses the model equations themselves to train (rather than an independent ground truth), some grain of salt is needed when interpreting its results: training is a non-convex optimization problem, the relative weighting between the loss terms can be delicate to tune, and a network can satisfy the PDE residual well while still converging to a physically implausible or trivial solution if the initial/boundary terms are not weighted carefully.