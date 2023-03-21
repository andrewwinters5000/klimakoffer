+++
title = "Milestone 1"
hascode = false
rss = "Description"
rss_title = "Milestone 1"
rss_pubdate = Date(2019, 5, 1)

tags = ["climatesystem"]
+++

# Milestone 1
\toc

## Introduction - Components of the Climate System

![](/assets/milestone1/ClimateSystem.png)
* Figure from lecture notes: [Stocker, "Introduction to Climate Modeling". Universität Bern](https://climatehomes.unibe.ch/~stocker/papers/stocker18icm.pdf).

### Atmosphere

<!-- Gasous part above the Earth's surface. The
atmosphere includes different substances in gaseous (e.g.
CO2), liquid (water, aerosols) or solid (dust) form.

Important processes are for instance:
* Weather 
* Radiation balance: incoming solar radiation, reflection (Albedo), Earth radiation, ...
* Formation of clouds and precipitation
* Turbulent atmospheric flow and heat transfer/mixing -->
The atmosphere is the gaseous layer above the Earth's surface and is composed of various substances in gaseous, liquid (such as water and aerosols), or solid (like dust) forms. It plays a crucial role in regulating the Earth's climate and supporting life on the planet.

Some of the important atmospheric processes include:

* Weather patterns, which involve the short-term changes in temperature, humidity, wind, and precipitation in a particular region.
* Radiation balance, which involves the absorption and reflection of incoming solar radiation, the Earth's albedo, and the emission of radiation from the Earth's surface.
* Cloud and precipitation formation, which are critical processes that help regulate the planet's climate.
* Turbulent atmospheric flow, which plays a crucial role in transferring heat and mixing various atmospheric constituents, thereby influencing weather patterns, cloud formation, and precipitation.

Overall, these processes work together to create a complex and dynamic atmosphere that is vital for sustaining life on Earth.

### Hydrosphere 
<!-- All forms of water above and below the Earth's surface This includes the whole global water cycle after precipitation has reached the surface


Important processes are for instance:

* Transport of ocean water masses, transport of heat.
* Change of inflow into different ocean basins.
* Connection between oceans and atmosphere., e.g. exchange of water vapour.
* Most important reservoir for carbon: oceans absorb a large amount of CO2: more than atmosphere and terrestial biosphere (plants and animals) combined. -->

The hydrosphere comprises all forms of water on and below the Earth's surface, including oceans, rivers, lakes, groundwater, and glaciers. It also includes the entire global water cycle, which begins when precipitation reaches the surface.

Several important processes occur within the hydrosphere, some of which are:

* Ocean water transport, which is responsible for the movement of water masses and heat around the globe.
* Changes in the inflow of water into different ocean basins, which can have a significant impact on ocean currents and climate patterns.
* The connection between the oceans and the atmosphere, which involves the exchange of water vapor and other gases.
* The absorption of carbon dioxide (CO2) by the oceans, which is the most crucial reservoir for carbon. The oceans absorb more CO2 than the atmosphere and the terrestrial biosphere (plants and animals) combined.

Overall, the hydrosphere plays a crucial role in regulating the Earth's climate and supporting life on the planet. Its processes and dynamics are essential to understanding the complex interactions between the Earth's atmosphere, oceans, and biosphere.


### Cryosphere
All forms of ice in the climate system including ice masses,
ice shelves, sea ice, glaciers and permafrost. The amount of total ice
has a strong impact on the hydrosphere (ice is a long term water reserve) and strongly affects the Albedo (reflection of sun radiation) and hence the radiation balance of the Earth,


### Land Surface 
The solid earth.
The location and position of the solid
earth (continents) is a determining
factor of climatic zones and defines
due to its shape the ocean currents.
It also affects the Albedo (reflectivity
of sand is different from rocks) and
is a reservoir of dust that might interact
with the atmosphere

### Biosphere 
Organic cover of the land masses (vegetation, soil, etc) and
marine organisms. Strong impact on carbon
exchange between different parts of Earth
hence strong impact on CO2 concentration.

Important processes:  
* Changes the reflectivity (Albedo) of the surface and, hence, the radiationbalance
* Regulates the water vapour transfer
* Vegetation is like having a rough surface, hence, impact on atmospheric flow (exchange of momentum).

### Anthroposphere
All interactions of humans that change processes or cause
new processes, e.g.,

* Emission of substances at a high rate.
* Land use change: deforestation, desertification, transformation into constructed areas, drainage of marshes.

In addition there are some external
forcing based on rare extreme events
like for instance emissions from volcanoes.

A complete climate model contains all
of the above components Furthermore
a coupling of all these components is
necessary for instance water vapour exchange


A complete climate model contains all
of the above components. Furthermore,
a coupling of all these components is
necessary (for instance, water vapour exchange).


@@colbox-red
**Bad news**

Every single process requires expert level
of research to understand the physics
and to generate model abstractions. We
could easily fill full lecture courses
on the individual components: the physics, 
the mathematical model the numerical
algorithms and their implementation.


A fully coupled globalclimate model
is out of the scope!!
@@

@@colbox-green
**Good news**

Not all research questions in climate sciece
require the full model. It is, however, part of the
scientific work to select a valid selection of
components and processes to get valid
answers that are scientifically robust.

With this introductory discussion on the climate
system, we come to the conclusion that to achieve
our goal "implement your own climate model from scratch" we need simplifications. To be more
precise: we will need strong simplifications!!
@@

**Comment**: For the interested student, we
recommend to attend other specialized courses
available at UoC or read detailed
lecture notes such as for instance: "Introduction to Climate Modeling" by Prof. Stocker, Physikalisches Institut, University of Bern (2016).

## Hierarchy of Climate Models

The combination of Atmosphere and Hydrosphere
(in particular oceans) with high-fidelity is termed
Global Climate Model / General Circulation Model (GCM).
As discussed above, these are, however, only two
components out of many. Hence, nowadays
the fullycoupled models that includes more
components and their interactions are termed
Earth System Models (ESM).

The high complexity of the Earth system not
only makes the approximation of the components
and their interaction very complicated and
involved (these code frameworks are huge with several persons' effort put in).
The actual computational power necessary to run these simulations
is extreme (Extreme scale Computing / Exascale
Computing).

@@colbox-blue
**Remark 1:** It is important to understand that, even
today, not all processes are fully understood. Hence,
their effect needs to be modeled as good
as possible.
@@

@@colbox-blue
**Remark 2:** Sometimes, the physics is well understood.
However in many cases nature is "multi-scale".
This means, for instance, that the spectra of
spatial sales range from centimeter and meter
up to 100 km.
We will learn that "resolution"
makes simulations expensive to run on a computer.
The resolution necessary to resolve all scales
is unfortunately prohibitive, even on the
most powerful super computers. Hence, all
simulations are under-resolved. Hence,
effects from small un-resolved scales are
missing. It is, therefore, necessary to model
the missing so called subgrid scales.
@@

@@colbox-blue
**Remark 3:** In the climate weather prediction
community, the modeling of components, processes
and subgrid sale effects is often called "parametrization".
The "model" often refers to the whole package:
PDEs+Numerics+Implementation (code/software).
@@

As mentioned above, the good news is that depending
on the science question, some components processes
are more important than others. Hence, with
enough expertise it is feasible to choose a
subset of physics and consider simplified
climate models.


It thus is not surprising that there is a huge
collection of simplified climate models developed
by different researchers in the last decades
Here is for instance a figure that lists a matrix
of simplifications with focus on Atmosphere+Hydrosphere:

![](/assets/milestone1/Models.png)
* Figure from lecture notes: [Stocker, "Introduction to Climate Modeling". Universität Bern](https://climatehomes.unibe.ch/~stocker/papers/stocker18icm.pdf).

## How do we choose a model?

Criteria to find a model for this course:

* It must be feasible to implement the model from scratch in 1 semester by students (ESM is out).
* We wanted to have a 2D grid to include earth surface modeling aspects, include localized predictions. Moreover, the topic of how to mesh the spheres is an important
decision for a grid based models in GCMs/ESMs.
* The physics, the numerics, and the computational
aspects should be accessible to a broad range
of students (math, physiscs, meteorology, geophysics, etc.)

**What model did we choose?**

From the criteria mentioned above, we
decided to go for a 2D Energy Balance Model (EBM),
which is a heavily simplified climate model
that estimates the average temperature
of the atmosphere at a grid node.

We mainly follow the paper
> Zhuang, K., North, G. R., & Stevens, M. J. (2017). A NetCDF version of the two-dimensional energy balance model based on the full multigrid algorithm. SoftwareX, 6, 198-202.


**See if we keep the following:**
We note that in this open source
publication the authors published a Fortran
code of there model Klimakofter jeand
the reference solutions of the milestones
are in many poetsvery close translations of this
code with differences in the numerics Strongest
deviation is the solver strategy for the linear
algebraicsystem that is not based on multigrid
but uses direct solver packages instead


## Sphere, Coordinats, Transforms and Grids

The shape of Earth is very close to a sphere (radius of about 6378 km) and hence the 
geometrical model of Earth is reasonably given by
a sphere in our climate model.

There are several conventions for
spherical coordinates. In the geographic coordinate system, we speak of latitude/colatitude and longitude. For
our model we will use the colatitude system.

* **Latitude**: North-south direction. Latitude lines are parallel to the equator and are assigned the angle from the equator.
* **Colatitude**: Complementary angle from a given latitude (meassured from the north pole).

| Location   | Latitude| Colatitude|
| -----------|---------|-----------|
| North pole | 90°     | 0°        |
| Equator    | 0°      |90°|
| South pole | -90° | 180°|

* **Longitude**: East-West direction. Longitude lines are perpendicular to the equator with range West -180° to East +180°.

@@colbox-blue
**Remark 1:** the values of longitude and latitude can be given in radians or degrees.
@@

![](/assets/milestone1/LongLat.png)
* **Source:** Wikipedia.


@@colbox-blue
**Remark 2:** In geography, the generation of a map
with long/lat values of a location always
depends on the choice of a reference system: the
so-called **geodetic datum**. The geodetic datum
is a reference ellipsoid. Only in
combination (map+geodetic datum) the
coordinates are precise and can be compared.
@@

![](/assets/milestone1/SphereCoord.png)

We consider real Cartesian ($x,y,z$) and spherical ($r,\theta,\varphi$) coordinates, and have following conventions:
* Radius: $r \in \R, \, 0 \le r < \infty$
* Colatitude: $\theta \in \R, \, 0 \le r < \pi$
* Longitude: $\varphi \in \R, \, 0 \le r < 2\pi$
with transformations:
\begin{align}
x &= r \sin \theta \cos \varphi, & r &= \sqrt{x^2 + y^2 + z^2},\\
y &= r \sin \theta \sin \varphi, & \theta &= \arctan \left(\frac{x^2 + y^2}{z} \right),\\
z &= r \cos \theta, & \varphi &= \arctan(y/z).
\end{align}

From analysis, we know that the Jacobian of the coordinate transformation is given by
\begin{align}
\partialderiv{x}{r} &= \sin \theta \cos \varphi, &
\partialderiv{x}{\varphi} &= -r \sin \theta \sin \varphi, & 
\partialderiv{x}{\theta} &= r \cos \theta \cos \varphi \\
\partialderiv{y}{r} &= \sin \theta \sin \varphi, &
\partialderiv{y}{\varphi} &= r \sin \theta \cos \varphi, & 
\partialderiv{y}{\theta} &= r \cos \theta \sin \varphi \\
\partialderiv{z}{r} &= \sin \theta \cos \theta, &
\partialderiv{z}{\varphi} &= 0, & 
\partialderiv{z}{\theta} &= -r \sin \theta,
\end{align}
and the respective Jacobian matrix,
\begin{align}
J =
\partialderiv{(x,y,z)}{(r,\theta,\varphi)} =
\begin{bmatrix}
\sin \theta \cos \varphi & -r \sin \theta \sin \varphi & r \cos \theta \cos \varphi \\
\sin \theta \sin \varphi & r \sin \theta \cos \varphi & r \cos \theta \sin \varphi \\
\sin \theta \cos \theta  & 0 & -r \sin \theta 
\end{bmatrix}
\in \R^{3 \times 3}
\end{align}
with the determinant
$$
|J|=r^2 \sin \theta,
$$
which can be used to ransform integrals
from Cartesian coordinates to spherical coordinates.

@@colbox-blue
**Example:** Volume of a sphere with radious R:
\begin{align}
\iiint_{V} \d V &= \iiint_{V} \d x \d y \d z \\
&= \int_{r=0}^R \int_{\theta=0}^{\pi} \int_{\varphi=0}^{2\pi} |J| \d r \d \theta \d \varphi\\
&= \frac{4\pi R^3}{3}
\end{align}
@@

It is important to note that the determinant can
get equal to zero for $\theta \in \{ 0, \pi\}$. From linear
algebra, we know that matrices with determinant
equal to zero are not regular, i.e., they cannot
be invented. Transformations where the Jacobian
matrix gets irregular are singular at this specific
locations. The locations $\theta=0$ (North) and $\theta=\pi$ (South)
correspond to the poles. Therefore, the transformation is
singular at the poles, which shows that, regarding
mappings, the poles are special locations and
are somewhat problematic when trying to
mesh the surface.
An illustration of converging grid lines
at the poles can be seen in the figure:

![](/assets/milestone1/PolesProblem.png)
* **Source**: Wikipedia

We can further observe from the figure that the
grid cells get smaller the closer they are to the
poles. So a regular grid in (co-)latitude and
longitude space gives an irregular grid on the
sphere surface.
In our model we will use this particular grid
(regular in la/lon) anyway and introduce
a special fix trick for the poles.
However, because of the issues discussed above,
there are many alternative ways of constructing
meshes for sphere:
![](/assets/milestone1/GridsSphere.png)
* **Source**: [www.encyclopedia-environment.org](http://www.encyclopedia-environment.org) ????

For instance, the famous ICON (Icosahedral Nonhydrostatic) model from the German weather service (DWD: Deutschen Wetterdienst) uses triangle
surface grids.
![](/assets/milestone1/ICONgrid.png)
* **Source**: [www.dwd.de](http://www.dwd.de)


As mentioned above, we will use a regulargrid for our
model. In so-called computational space, we consider
our coordinate directions as either latitude/colatitude and longitude:
![](/assets/milestone1/OurGrid.png)


We define the number of grid lines as
\begin{align}
\nlong \in \mathbb{N} \\
\nlat \in \mathbb{N}
\end{align}
to get the size of the grid cells as
\begin{align}
\Delta \varphi &= \frac{2\pi}{\nlong-1} \\
\Delta \theta &= \frac{\pi}{\nlat -1}
\end{align}
and the grid node locations as
\begin{align}
\varphi_i &= -\pi + (i-1) \Delta \varphi, & i&=1, 2, \ldots, \nlong,\\
\theta_j &= -\frac{\pi}{2} + (j-1) \Delta \theta, & j&= 1, 2, \ldots, \nlat.
\end{align}

To illustrate the results of the model,
we could directly plot in computational space.
However, it is more pleasing to the eyes and
more common to plot the results in physical
space (or an approximation to that).
There are many options available in the literature
to get from lat/long to other coordinates.
In this course we all use the so-called Robinson
projection, which is an interesting one as this
transform has no mathematical properties (e.g, keep distances, keep angles, keep area) but
was designed by Robinson by hand to look
pleasing to his eyes(!).

While Robinson provided a translation
table for values (lat/lon), there are
closed form approximations available.
The form we consider was presented by
Beineke in 1991 "Untersuchungen zur Robinson-Abbildung and Vorschlag einen analytischen
Abbildungsvorschrift".

The approximation that Beineke proposes
is based on a polynomial spline approximation.
Given the computational coordinates, he defines the new coordinates of the
curvilinear grid as
\begin{align}
    \hat{x}_{ij} &= (d + e \theta_j^2 + f \theta_j^4 + g \theta_j^6) \varphi_i \\
    x &= \frac{180}{\pi} \frac{\hat{x}_{ij}}{\max_{i,j} (\hat{x}_{ij})} \\
    \hat{y}_{ij} &= a \theta_j + b \texttt{sign} (\theta_j) |\theta_j|^c \\
    y &= 90 \frac{\hat{y}}{\max_{i,j} (\hat{x}_{ij})}
\end{align}
with the parameters
\begin{align}
a =&  0.96047, &
    b =& -0.00857, &
    c =&  6.41, \\
    d =&  2.6666, &
    e =& -0.367, &
    f =& -0.150 \\
    g =&  0.0379.
\end{align}

Applying the simplified Robinson
projection to the computational grid
gives a curvilinear mesh a shown in the
figure:
![](/assets/milestone1/Robinson.png)
* **Source**: Ipbuker, C. (2005). A computational approach to the Robinson projection. Survey Review, 38(297), 204-217.

As can be seen in the figure, the
geographic map can be used to
display the land-sea-ice-show
mask of Earth, which is the
topic of the first milestone.

**NOTE:** Explain that the grid does NOT contain 180°!!!