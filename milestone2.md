+++
title = "Milestone 2"
hascode = true
rss = "Description"
rss_title = "Milestone 2"
rss_pubdate = Date(2022, 5, 1)

tags = ["ebm", "solar radiation", "orbital parameters"]
+++

# Milestone 2
\toc

## Conservation and Balance 

Many processes in nature and engineering can be modeled (described) with a simple principle: the principle of **conservation**. Consider a closed domain $\Omega\in\mathbb{R}^n$ and a quantity $u=u(x,t)\in\mathbb{R}$ that is defined for all $x\in\Omega$ and $t\geq 0$. The function $u(x,t)$
typically describes a physical quantity such as mass, momentum, or for instance energy.

We are interested in modeling the temporal evolution (change in time t). Observations of nature of the behaviour of such quantities lead to the
following simple principle:
@@colbox-blue
**Observation:** The temporal change of $u(x,t)$ in a sub-domain $\omega\subset\Omega$ is equal to the amount
that gets generated or destroyed inside of $\omega$ in addition to the flux balance
inside out of $\omega$ through the surface/boundary $\partial\omega$.
@@

The quantity of $u$ changes, if: 

(i) There is a positive/negative source inside of the sub-domain $\omega$

(ii) There is a positive/negative flux balance through the boundary of the sub-domain $\partial\omega$

> HERE IS STUFF MISSING

@@colbox-blue
**Remark 1:** We call this the integral formulation of the problem.
@@

@@colbox-blue
**Remark 2:** The flux function $\vec{f}$ typically depends on the solution $u$ and the variables $x,t$, i.e., $\vec{f} = \vec{f}(u,x,t)$.
@@

If we make the mathematical assumption that the function $u(x,t)$ is sufficiently smooth (such that we can take the derivatives in space
and time), we can apply the Gauss integral theorem to the surface integral

> HERE IS STUFF MISSING

As we have chosen an arbitrary sub-domain $\omega$ with no special properties, the equation needs to hold for all choices of $\omega\subset\Omega$. This
can only be true if the integrands balance out to zero, hence
$$
\frac{\partial u}{\partial t} + \vec{\nabla}\cdot\vec{f} = S,\quad x\in\Omega,\,\,t\in\mathbb{R}^+.
$$

@@colbox-blue
**Remark 3:** This is a partial differential equation (PDE) in space and time and is typically called a balance law.
@@

@@colbox-blue
**Remark 4:** For many processes, the source term can be neglected, i.e., we can choose $S(x,t) = 0$. The resulting PDE describes processes, where the quantity $u$ is neither destroyed or generated, but is only changing by fluxes. Such PDEs are called conservation laws
$$
\frac{\partial u}{\partial t} + \vec{\nabla}\cdot\vec{f} = 0,\quad x\in\Omega,\,\,t\in\mathbb{R}^+.
$$
@@

Depending on the process we want to model, we need to chose the quantity o finterest $u(x,t)$, a model for the flux $\vec{f}(u,x,t)$  and a model for the source term $S(u,x,t)$. There are 
many examples of such models, e.g., mass and momentum conservation in fluid mechanics. We consider here as an exaple the so-called heat equation, or heat transfer equation. 

For the heat equqation we are interested in the change of temperature $T(x,t)$ (which is strongly related to the internal energy of a body) in space and time, hence our choice for the unknown quantity is $u = T$. Next, we need a model for the flux. Jean Babtiste Joseph Fourier (1822) gave a model for the heat flux, where the flux of heat is negative proportional to the temperature difference (heat goes from high temperatures to lower temperatures), i.e. 

> HERE IS STUFF MISSING

@@colbox-blue
**Remark 5:** A very simple version of the heat equation results in 1D space ($x_1 = x$) with a constant diffusion coefficient $d=const$
$$
T_t - \frac{\partial}{\partial x}(d\,T_x) = T_t - d\,T_{xx} = 0.
$$
@@

For scalar PDEs with two independent variables x and t of second order
(the maximum derivatives are second order derivatives) it is common to distinguish
between different types of PDEs. Assuming a scalar second order PDE of the general form 
$$
a u_{xx} + b u_{xt} + c u_{tt} + d u_x + e u_t + f u + g = 0,
$$
we can define the quantity 
$$
\Delta(x,t) = a(x,t)\,c(x,t) - \frac{b(x,t)^2}{2}
$$
to get a classification of the different types

(i) $\Delta(x,t) > 0$, the PDE is elliptic in $(x,t)$

(ii) $\Delta(x,t) = 0$, the PDE is parabolic in $(x,t)$

(iii) $\Delta(x,t) < 0$, the PDE is hyperbolic in $(x,t)$

If we consider again our simple 1D constant coefficient heat equation and compute its type, we get $\Delta(x,t) = 0\quad\forall (x,t)$. Hence, the **heat equation is a parabolic PDE**. 

In general, parabolic PDEs model processes that evolve in time and are **not** reversible in time, such as friction, diffusion, dissipation, etc. The effect over time is a "smearing" of the quantity, smooting out of large gradients and extrema. 


## Solar forcing

Previously, we have made the assumption that the solar forcing term remains constant across both space and time. However, this assumption overlooks the fact that the Earth's position and orientation in relation to the sun changes throughout the year, leading to a variation in the amount of incoming insolation. The two primary factors that contribute to the variability of solar radiation received by the Earth are as follows:

1. **Distance from the sun**: Rather than a perfect circle, the Earth's orbit around the sun is an ellipse. Consequently, the distance between the Earth and the sun fluctuates throughout the year, leading to a change in the total amount of solar radiation that reaches the Earth.

2. **Tilted axis of rotation**: Due to the Earth's tilted axis of rotation, different parts of the planet receive varying amounts of solar radiation as it orbits the sun (depending on the latitude). This phenomenon gives rise to the changing seasons.

The derivations presented in this section can be found in the following references:

> Berger, A. (1978). Long-term variations of daily insolation and Quaternary climatic changes. Journal of Atmospheric Sciences, 35(12), 2362-2367.

**TODO**: Add more references!!

### Important definitions

![](/assets/milestone2/Orbits.png)

Before we delve into calculating the impact of the Earth-sun distance and Earth's axis tily on the solar radiation on Earth, let us define some relevant concepts (see figure above for reference):

* Perihelion: The point in Earth's orbit where it is closest to the Sun. Currently, the perihelion occurs around January 4th.
* Aphelion: The point in Earth's orbit where it is farthest from the Sun. Currently, the aphelion occurs around July 6th.
* Ecliptic: The plane of Earth's orbit around the Sun.
* Northern summer solstice: The point in Earth's orbit where the longest day of the year occurs in the Northern Hemisphere and the shortest day of the year occurs in the Southern Hemisphere. At this point, the plane formed by the rotation axis of Earth and the line that connects Earth and the Sun is perpendicular to the ecliptic. Currently, the Northern summer solstice occurs around June 21st.
* Northern winter solstice: The point in Earth's orbit where the shortest day of the year occurs in the Northern Hemisphere and the longest day of the year occurs in the Southern Hemisphere. At this point, the plane formed by the rotation axis of Earth and the line that connects Earth and the Sun is perpendicular to the ecliptic. Currently, the Northern winter solstice occurs around December 21st.
* Vernal equinox: The point in Earth's orbit where the line that connects Earth and the Sun aligns with the equatorial plane of Earth during the transition from winter to summer in the Northern Hemisphere. This is also the moment when Earth's rotation axis is directly perpendicular to the Sun-Earth line.
* Northern autumnal equinox: The point in Earth's orbit where the line that connects Earth and the Sun aligns with the equatorial plane of Earth during the transition from summer to winter in the Northern Hemisphere. This is also the moment when Earth's rotation axis is directly perpendicular to the Sun-Earth line.
* True longitude of earth ($\lambda$): Position of Earth at a given time as meassured from the vernal equinox. The position $\lambda = 0$ is considered the begining of an _astronomical year_.

To compute the distance from the sun and Earth's axis tilt angle, we need to consider three parameters that vary over time as a result of the gravitational interactions between Earth and other celestial bodies within the solar system. We call these parameters the **orbital parameters** and define them as

1. Eccentricity ($e$): This parameter determines the degree to which Earth's orbit around the sun deviates from a perfect circle. It is computed as
    $$\label{eq:ecc}
    e = \sqrt{1-\frac{b^2}{a^2}},
    $$ 
    where $a$ represents the semi-major axis, and $b$ represents the semi-minor axis of the ellipse (refer to the figure). Earth's eccentricity undergoes periodic changes over hundreds of thousands of years.
2. Obliquity ($\epsilon$): This parameter, also referred to as axial tilt, represents the angle between Earth's rotational axis and its orbital axis. The obliquity angle is equivalent to the angle between the equatorial plane and the orbital plane. The obliquity angle varies periodically over approximately $\tau_{\epsilon} \approx 20,000$ years.
3.  Precession distance ($\tilde \omega$): Earth's axis rotates with a period of about $40,000$ years, causing the seasons to shift in position within the elliptical orbit of Earth. This phenomenon is known as precession or spin. We define the precession distance as the angle between the aphelion and the vernal equinox.

> **NOTE:** In the paper of Berger, the precession distance ($\tilde \omega$) is sometimes defined from the perihelion and sometimes from the aphelion. We use the aphelion in our implementation as it is the one obtained with equation (6) from Berger.

![](/assets/milestone2/part2-earthspin-nolabel.jpg)
* Figure modified from [https://ugc.berkeley.edu/background-content/earths-spin-tilt-orbit/](https://ugc.berkeley.edu/background-content/earths-spin-tilt-orbit/).

In the following sections, we will assume that the eccentricity, obliquity and precession distance are constant to derive the total solar irradiance.
This is a reasonable assumption for climate simulations in which the orbital parameters are updated at the time interval $\Delta t_{\text{orb}} \ll \tau_{\epsilon}$. 

### Effect of Earth's distance to the sun



<!-- As we saw in the [Radiation Section](#radiation) -->
The inverse-square law states that the total radiation radiation that is received from a source is inversely proportional to the square of the distance from source.

![](/assets/milestone2/Inverse_square_law.png)
* Source: Wikipedia

As a result, the total radiation that is received at the top layer of Earth's atmosphere is 
$$
S_r(t) = \frac{r_0^2}{r^2} S_0,
$$
where $r$ is the (time-dependent) Earth-sun distance, $r_0 \approx a$ is roughly the mean Earth-sun distance (defined as one anstronomical unit), and $S_0$ is the so-called solar constant, the mean solar elecromagnetic radiation per unit area meassured on a surface perpendicular to the solar rays at a distance $r_0$. 

Since Earth's orbit is an ellipse and the sun sits in one focus, we can calulate the Earth-sun distance as
$$\label{eq:r}
r = \frac{a (1-e^2)}{1 - e \cos (\nu)},
$$
where the position (angle) of earth with respect to the aphelion is
$$\label{eq:nu}
\nu = \lambda - \tilde \omega
$$
The radiation at the top of the atmosphere is then computed as
$$
S_r(t) %= \frac{(1-e \cos (\nu))^2}{(1 - e^2)^2} S_0 
= \frac{(1-e \cos (\lambda - \tilde \omega))^2}{(1 - e^2)^2} S_0.
$$



### Effect of Earth's axial tilt

Due to Earth's axial tilt, the solar irradiance depends on the latitude and the time.

We call the angle between the Earth-sun line and the equatorial plane of Earth _declination angle_ and note it with $\delta$. This angle changes throughout the year, as the Earth revolves around the sun (see figure):

![](/assets/milestone2/Declination.png)

In general, the declination angle can be computed as
$$
\sin (\delta) = \sin (\lambda) \sin (\epsilon).
$$

Depending on the declination angle and the latitude, we identify three regions of interest:


#### (1) Latitudes where there is no sunrise (winter)
There is no incoming solar radiation for latitudes that fulfill
$$
|\lat| + |\delta| \ge \frac{\pi}{2} \,\, \text{with} \,\, \lat \delta < 0,
$$
or equivalently
$$
z = -\tan(\lat)\tan(\delta) \ge 1.
$$

For these latitudes, the insolation is simply
$$
S(\lat,t) = 0.
$$


#### (2) Latitudes where there is no sunset (summer)
Some regions of earth are exposed to incoming solar radiation throughout the entire day during part of the year. These regions fulfill
$$
\label{eq:nosunset}
|\lat| + |\delta| \ge \frac{\pi}{2} \,\, \text{with} \,\, \lat \delta > 0,
$$
or equivalently
$$
z = -\tan(\lat)\tan(\delta) \le -1.
$$

The calculation of the effective insolation is more involved, as it requires the use of differential geometry. The result reads as
$$
S(\lat,t) = S_r(t) \sin(\lat) \sin(\delta).
$$

#### (3) Latitudes where there is daily sunrise and sunset
There is daily sunrise and sunset at latitudes that fulfill the condition
$$
- \left( \frac{\pi}{2} - |\delta| \right) < \lat < \frac{\pi}{2} - |\delta|.
$$

For these latitudes, the calculation of the insolation also requires the use of differential geometry. The result reads as
$$
S(\lat,t) = S_r(t) \frac{1}{\pi} (H_0 \sin(\lat) \sin(\delta)+\cos(\lat) \cos(\delta) \sin(H_0)),
$$
with the absolute angle of the sun at sunrise and sunset
$$
H_0 = \arccos (z).
$$

### Bonus: Computation of the true longitude $\lambda$

Kepler's second law states that a line segment joining a planet and the Sun sweeps out equal areas during equal intervals of time. Therefore, Earth moves faster when it is closer to the sun. Is a short time interval $\d t$, the area swept is equal to the area of a triangle with base $r \d \nu$ and height $r$. Therefore, ee can write Kepler's second law as
$$\label{eq:dAdt}
\frac{\d A}{\d t} = \frac{\pi a b}{T} = \frac{r^2}{2} \frac{\d \nu}{\d t},
$$
where $\pi a b$ is the total area of a ellipse, which is swept in a complete period $T$.

Assuming that the time is meassured in years and replacing the definition of the Earh-sun distance \eqref{eq:r} and the eccentricity \eqref{eq:ecc} in \eqref{eq:dAdt} we obtain
$$
\frac{\d \lambda}{\d t} = \frac{2\pi}{(1 - e^2)^{3/2}} (1 - e \cos (\lambda - \tilde \omega))^2.
$$

## Time discretization

In our simple climate model, we will use 48 time steps each year and set the first time step as the vernal equinox. For such a time-discretization with 48 time steps, the main astronomical events and their correspondence with time steps are listed in the following table:

|  Astronomical event |   Time step|
| ------------------ | -----------| 
|   Vernal Equinox   |   1        |  
|   Summer Solstice  |   13       | 
|   Autumnal Equinox |   25       | 
|   Winter Solstice  |   37       | 

In addition, the following table presents the time steps that correspond to each month:

| Month |     Time Steps  | 
|-------|-----------------|
| Jan   |  38, 39, 40, 41 |
| Feb   |  42, 43, 44, 45 |
| Mar   |  46, 47, 48   1 |
| Apr   |   2,  3,  4,  5 |
| May   |   6,  7,  8,  9 |
| Jun   |  10, 11, 12, 13 |
| Jul   |  14, 15, 16, 17 |
| Aug   |  18, 19, 20, 21 |
| Sep   |  22, 23, 24, 25 |
| Oct   |  26, 27, 28, 29 |
| Nov   |  30, 31, 32, 33 |
| Dec   |  34, 35, 36, 37 |
