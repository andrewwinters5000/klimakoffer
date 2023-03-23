+++
title = "Milestone 2"
hascode = true
rss = "Description"
rss_title = "Milestone 2"
rss_pubdate = Date(2022, 5, 1)

tags = ["ebm", "solar radiation", "orbital parameters"]
+++

# Milestone 2 - Radiation modeling

\toc

## Introduction

The energy balance of Earth is strongly impacted by radiation. The following figure shows the energy fluxes in the global Earth-atmosphere system

\fig{/assets/milestone2/ClimateSystem.png}
* Figure from [Trenberth, K. E., Fasullo, J. T., & Kiehl, J. (2009). Earth's global energy budget. Bulletin of the American Meteorological Society, 90(3), 311-324](https://journals.ametsoc.org/downloadpdf/journals/bams/90/3/2008bams2634_1.pdf).

In our EBM, we aim to include four effects: 

(i) Incoming solar raditaion. 

(ii) Reflection of radiation by the surface and cloud cover. 

(iii) Cooling because of outgoing longwave radiation. 

(iv) Effect of greenhouse gases (mainly $CO_2$).

## Outgoing longwave radiation 

The goal in this section is to define a model/parametrization for the source term $S_{OLW}(T,x,t)$. 

But first, to warm up with the topic, we consider as a toy model an idealized black-body Earth, i.e., we assume that the Earth is a _black body_ that emits radiation in the infrared spectrum.

The radiation energy per time that is emitted by a black body can be computed by the Stefan-Boltzmann law of physics 
$$
I = \sigma_{SB}\,T_R^4,
$$
where $I$ is the radiation energy per time per area with units $[W/m^2]$, $T_R$ is the radiation temperature with physical units Kelvin $[K]$, $\sigma_{SB} = 0.56687\cdot 10^{-8}$ is the Stefan-Boltzmann constant with units $[W/m^2/K^4]$.

For this idealized black-body Earth, the temperature is determined when the outgoing radiation is in equilibrium/balance with the incoming stellar radiation. The amount of incoming energy can be roughly estimated as $S_0\,(1-\alpha)\,\pi\,R_E^2$, where $S_0 = 1360$ is the solar constant (the mean solar elecromagnetic radiation received on Earth with units $[W/m^2]$), $\alpha$ is the surface albedo (the amount of the solar radiation that is reflected back to space) with the planetary average being about $\alpha=0.3$ (more details in the [next section](#albedo)), and $R_E=6.378\cdot 10^{6}$ is the radius of Earth in units [m]. 

The amount of outgoing energy is $\sigma_{SB} T_R^4 4\,\pi\,R_E^2$, and we get our first (simplest version of an) EBM
$$\label{eq:blackbody}
\sigma_{SB} T_R^4 4\,\pi\,R_E^2 = S_0\,(1-\alpha)\,\pi\,R_E^2.
$$
We can relate this simple EBM \eqref{eq:blackbody} to the general form \eqref{eq:EBM} by making the assumption of thermodynamic equilibrium (no temporal change $\partial T / \partial t= 0$), no heat diffusion ($d = 0$), and the following choice of source terms: 
\begin{align}
S_{sol} &= S_0\,(1-\alpha)\,\pi\,R_E^2, \\
S_{OLW} &= - \sigma_{SB} T_R^4 4\,\pi\,R_E^2.
\end{align}

We can directly solve \eqref{eq:blackbody} to get the equilibrium solution
$$
T_R = \left(\frac{S_0}{4}\frac{(1-\alpha)}{\sigma_{SB}}\right)^{\frac{1}{4}}\approx 255\, [K] = -18\, [^\circ C].
$$
This model is indeed as simple as it gets and it is no surprise that the quality of the prediction of an average Earth temperature is quite off. The blackbody radiation temperature of Earth would be only about $-18$ degree Celsius, hence, some major modeling improvements are necessary. 

## Budyko's Empirical infrared Model
Budyko (1968) suggested an empirical linear model for the outgoing longwave radiation 
$$
I \sim A + B\, T.
$$
It is in general motivated by available observational data, shown in the next figure

\fig{/assets/milestone2/OutgoingLongwaveRadiation.png}
* Figure is from the book _North, G. R., & Kim, K. Y. (2017). Energy balance climate models. John Wiley & Sons_ and is originally from [Graves, C. E., Lee, W. H., & North, G. R. (1993). New parameterizations and sensitivities for simple climate models. Journal of Geophysical Research: Atmospheres, 98(D3), 5025-5036](https://agupubs.onlinelibrary.wiley.com/doi/pdfdirect/10.1029/92JD02666?casa_token=X0WG_pxk8AUAAAAA:2mvPv6HgmsA467qq44RYKY8WrJZLh_Bl-lN2kzgdBLJi3-xSVh0il6g-p1PSlxda51H8YVdkx1dsxSI).

The figure shows infrared radiation density plots averaged monthly, measured by satellite compared to the surfacetemperature at the same month and location. 
(a) shows the whole sky (including clouds) and (b) shows only the clear (cloudless) sky.

If we consider the temperature in units Kelvin, we can fit the observed data with the linear model by choosing good constants $A$, and $B$ to get 
$$
I_{IR/OLW} = A + B\,(T - 273),
$$
with $A=210.3$ as the radiative cooling in units $[W/m^2]$, and $B=2.15$ the radiative cooling feedback with units $[W/m^2/K]$. It is important to note, that the choice of this parameters have a direct impact on the outgoing radiation and hence on the cooling. Several others have fitted the data differently, hence some range of choices is available. The values we selected are from the paper by Zhuang et al. (2017).

We are now able to consider a second, but hopefully improved toy EBM. We replace the crude blackbody radiation with a phenomenological approximation of the outgoing radiation, the Budyko model to get 
$$
(A + B\,(T_R - 273)) 4\,\pi\,R_E^2 = S_0\,(1-\alpha)\,\pi\,R_E^2,
$$
which can be directly solved again to get the equilibrium temperature
$$
T_R = \frac{\frac{S_0}{4}(1 - \alpha) - A}{B} + 273 \approx 13\,[^\circ C].
$$

@@colbox-blue
**Remark 8:** As discussed, we have introduced a data driven model for our outgoing longwave radiation energy change. We introduced an ansatz with parameters (parametrization) and used real world measurements/observations to select the parameters, i.e., to fit the model.
@@

@@colbox-blue
**Remark 9:** The phenomenological model of Budyko drastically improves the temperature prediction of Earth from the crude blackbody temperature of $-18$ to the temperature $13^\circ C$, compared to the observed value of about $14.5^\circ C$.
@@

## Effect of greenhouse gases ($CO_2$)

For the interested reader, we refer to chapter 4 of the book by Kim and North, "Energy Balance Climate Model", (2017, Wiley) and the following paper 

> [Myhre, G., Highwood, E. J., Shine, K. P., & Stordal, F. (1998). New estimates of radiative forcing due to well mixed greenhouse gases. Geophysical research letters, 25(14), 2715-2718](https://agupubs.onlinelibrary.wiley.com/doi/pdfdirect/10.1029/98GL01908).

The main constituents of the atmosphere: $N_2$, $O_2$, and $Ar$ do not absorb strongly in the infrared, as the diatomic molecules ($N_2$, $O_2$) have no permanent dipole and
$Ar$ has no modes of rotation/vibration in the infrared spectrum. $H_2O$ molecules have a permanent dipole, which makes it respond strongly to passing electromagnetic waves.
Carbondioxide ($CO_2$), methane ($CH_4$), and nitreous oxide ($NO_2$) do not have a permanent dipole, but they can have induced dipole moments which then may lead to infrared absorbtion. 

@@colbox-blue
**Comment:** The effect of greenhouse gases is very complex with ongoing research. $H_2O$ in particular is very important but ever so complex due to it being dependent on many other components and processes, i.e., the full water cycle. We will consider in our EBM only the affect of $CO_2$ on the radiation. Infrared absorbtion means that the efficiency of our outgoing radiation (cooliong effect) decreases (which causes a higher equilibrium temperature). This decrease in efficiency is topic of many investigations and studies, e.g., by the IPCC.
@@

In this course, we follow the paper by Myhre et al. (1998) to define our parametrization of the greenhouse gas effect. From this paper, we first look at the effect of the amount of greenhouse gases measured in parts per million $[ppm]$, as plotted in the following figure

\fig{/assets/milestone2/CO2forcing.png}
* Figures from Myhre et al. (1998)

The figures show radiative forcing as a function
of concentration [ppm] for $CO_2$, $CH_4$, $N_2O$.

Myhre et al. and also other research groups
introduced simplified expressions that
parametrize the effect

\fig{/assets/milestone2/CO2e.png}
* Table from Myhre et al. (1998)

As mentioned, we only consider the effect of $CO_2$ in our model and hence choose the approximation 
$$
\Delta T = \alpha_{\text{Myhre}}\, \ln(CO_2/CO_2(t_0)),
$$
where 
$$
\alpha_{\text{Myhre}} = 5.35\,[W/m^2]
$$
and $CO_2$ is the concentration in $[ppm]$ and $CO_2(t_0) = 315\, [ppm]$ is the reference concentration in the year $1950$.

In summary, we get the following parametrization of our outgoing longwave radiation source term 
$$
S_{OLW}(T,x,t,CO_2) = -(A + B\, (T - 273) - \Delta F(CO_2)),
$$
which we reformulate into the shorthand notation
$$
S_{OLW}(T,x,t,CO_2) = - (A(CO_2) + B\,T),
$$
where
$$
A(CO_2) := 210,3 - 5.35\,\ln(CO_2/315))\,\,[W/m^2]
$$
and 
$$
B = 2.15\,\,[W/m^2/K]
$$
where we further made the assumption that the unit of the temperature $[T] = [^\circ C]$ instead of Kelvin.

