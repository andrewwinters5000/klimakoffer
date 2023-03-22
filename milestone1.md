+++
title = "Milestone 1"
hascode = false
rss = "Description"
rss_title = "Milestone 1"
rss_pubdate = Date(2019, 5, 1)

tags = ["climatesystem"]
+++

# Milestone 1
In this milestone, we will learn about the climate system and different climate models that describe it.
At the end of the chapter, we will select a climate model for the course and introduce some basic concepts about the mesh and visualization.

\toc

## Introduction 
### Components of the Climate System

The Earth's climate is a complex system that redistributes the energy (hear) from the sun throughout the planet. This energy transfer is carried out by various components, including the atmosphere, hydrosphere, cryosphere, land surface, and biosphere. Each of these components plays a crucial role in regulating the Earth's climate, and changes to any one of them can have far-reaching effects on the system as a whole. 
In addition, human activities affect climate on Earth significantly and are nowadays considered an additional component: the anthroposphere.
Understanding how these components interact with each other is essential to comprehending the complex processes that govern the Earth's climate.

\fig{/assets/milestone1/ClimateSystem.png}
<!-- ![](/assets/milestone1/ClimateSystem.png) -->
* Figure from lecture notes: [Stocker, "Introduction to Climate Modeling". Universität Bern](https://climatehomes.unibe.ch/~stocker/papers/stocker18icm.pdf).

#### Atmosphere

The atmosphere is the gaseous layer above the Earth's surface and is composed of various substances in gaseous, liquid (such as water and aerosols), or solid (like dust) forms. It plays a crucial role in regulating the Earth's climate and supporting life on the planet.

Some of the important atmospheric processes include:

* Weather patterns, which involve the short-term changes in temperature, humidity, wind, and precipitation in a particular region.
* Radiation balance, which involves the absorption and reflection of incoming solar radiation, the Earth's albedo, and the emission of radiation from the Earth's surface.
* Cloud and precipitation formation, which are critical processes that help regulate the planet's climate.
* Turbulent atmospheric flow, which plays a crucial role in transferring heat and mixing various atmospheric constituents, thereby influencing weather patterns, cloud formation, and precipitation.

Overall, these processes work together to create a complex and dynamic atmosphere that is vital for sustaining life on Earth.

#### Hydrosphere 

The hydrosphere comprises all forms of water on and below the Earth's surface, including oceans, rivers, lakes, groundwater, and glaciers. It also includes the entire global water cycle, which begins when precipitation reaches the surface.

Several important processes occur within the hydrosphere, some of which are:

* Ocean water transport, which is responsible for the movement of water masses and heat around the globe.
* Changes in the inflow of water into different ocean basins, which can have a significant impact on ocean currents and climate patterns.
* The connection between the oceans and the atmosphere, which involves the exchange of water vapor and other gases.
* The absorption of carbon dioxide (CO2) by the oceans, which is the most crucial reservoir for carbon. The oceans absorb more CO2 than the atmosphere and the terrestrial biosphere (plants and animals) combined.


#### Cryosphere

The cryosphere refers to all forms of ice in the Earth's climate system, including ice masses, ice shelves, sea ice, glaciers, and permafrost. The amount of ice present in the cryosphere has a significant impact on the hydrosphere, as it serves as a long-term water reserve that can affect water availability in different regions of the world. In addition, the cryosphere plays a crucial role in regulating the Earth's radiation balance through its effect on the planet's albedo, or the reflection of incoming solar radiation. Changes in the cryosphere can lead to alterations in the planet's albedo, which can have significant consequences for global temperature and climate patterns. Therefore, understanding the dynamics of the cryosphere and its relationship with other components of the climate system is essential for predicting and mitigating the effects of climate change.


#### Land Surface 

The Land Surface refers to the solid portion of the Earth's crust. The location and positioning of the continents have a significant impact on the distribution of climatic zones across the planet, as well as the formation and direction of ocean currents. Additionally, the Land Surface plays a critical role in regulating the Earth's radiation balance through its effect on the planet's albedo, which can vary depending on the type of terrain (e.g., sand versus rocks). The Land Surface also acts as a reservoir of dust particles that can interact with the atmosphere and affect weather patterns. Understanding the Land Surface and its interactions with the other components of the Earth's climate system is essential for predicting and mitigating the effects of climate change.

#### Biosphere 
The Biosphere refers to the organic cover of the Earth's land masses, including vegetation, soil, and marine organisms. It has a strong impact on carbon exchange between different parts of the Earth and can significantly affect the concentration of CO2 in the atmosphere. Some of the key processes that the Biosphere is involved in include:

* Changing the reflectivity (Albedo) of the Earth's surface, which can have a significant impact on the planet's radiation balance.
* Regulating the transfer of water vapor between the land and the atmosphere, which can affect weather patterns and climate.
* Vegetation acts like a rough surface, which can impact atmospheric flow and the exchange of momentum between the land and the atmosphere.

Understanding the role of the Biosphere in the Earth's climate system is critical for predicting and mitigating the effects of climate change.

#### Anthroposphere

The Anthroposphere is the term used to describe all the interactions and activities of humans that change existing processes or create new ones within the Earth's climate system. This includes activities such as the high-rate emission of substances, changes in land use, including deforestation, desertification, the conversion of natural habitats into constructed areas, and the drainage of marshes. These human activities can have significant impacts on the Earth's climate and ecosystems, affecting factors such as greenhouse gas emissions, water availability, and the balance of biodiversity. 

Apart from the components mentioned earlier, there are additional components that can significantly impact the Earth's climate system. These components are based on rare and extreme events, such as volcanic eruptions, which can release large amounts of gases and particles into the atmosphere. These emissions can have short-term effects on the planet's temperature and weather patterns by altering the amount of solar radiation that reaches the Earth's surface. Volcanic eruptions can also have long-term impacts by contributing to changes in the Earth's albedo and carbon cycle. Therefore, while such events may be infrequent, they play an important role in shaping the Earth's climate system

-------

A complete climate model contains all
of the above components. Furthermore,
the interaction between all these components is
necessary (for instance, water vapour exchange).


@@colbox-red
**Bad news**

Every single process requires expert level
of research to understand the physics
and to generate model abstractions. We
could easily fill full lecture courses
on the individual components: the physics, 
the mathematical model, the numerical
algorithms and their implementation, etc.


As a result, a fully coupled global climate model
is out of the scope of this course!
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
lecture notes such as for instance: ["Introduction to Climate Modeling" by Prof. Stocker, Physikalisches Institut, University of Bern (2016)]((https://climatehomes.unibe.ch/~stocker/papers/stocker18icm.pdf)).

### Hierarchy of Climate Models

The combination of Atmosphere and Hydrosphere models
(in particular oceans) with high-fidelity is termed
Global Climate Model / General Circulation Model (GCM).
As discussed above, these are, however, only two
components out of many. Hence, nowadays
the fully coupled models that includes more
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
by different researchers in the last decades.
Here is, for instance, a figure that lists a matrix
of simplifications with focus on Atmosphere+Hydrosphere:

![](/assets/milestone1/Models.png)
* Figure from lecture notes: [Stocker, "Introduction to Climate Modeling". Universität Bern](https://climatehomes.unibe.ch/~stocker/papers/stocker18icm.pdf).

### How did we choose a model?

We used the following criteria to find a model for this course:

* It must be feasible to implement the model from scratch in one semester by students (ESM is out).
* We want to have a 2D grid to include earth surface modeling aspects and localized predictions. Moreover, the topic of how to mesh the spheres is an important decision for a grid based models in GCMs/ESMs.
* The physics, the numerics, and the computational aspects should be accessible to a broad range of students (math, physiscs, meteorology, geophysics, etc.)

**What model did we choose?**

From the criteria mentioned above, we
decided to go for a 2D Energy Balance Model (EBM),
which is a heavily simplified climate model
that estimates the average temperature
of the atmosphere at location on the surface of earth using a _partial differential equation_.

In our course, we will mainly follow the paper
> Zhuang, K., North, G. R., & Stevens, M. J. (2017). A NetCDF version of the two-dimensional energy balance model based on the full multigrid algorithm. SoftwareX, 6, 198-202.


<!-- **See if we keep the following:**
We note that in this open source
publication the authors published a Fortran
code of there model Klimakofter jeand
the reference solutions of the milestones
are in many poetsvery close translations of this
code with differences in the numerics Strongest
deviation is the solver strategy for the linear
algebraicsystem that is not based on multigrid
but uses direct solver packages instead -->


## Spherical coordinates and grids

The shape of Earth is very close to a sphere with radius of about 6378 km. Therefore, the geometrical model of Earth is reasonably given by the surface of a sphere in our 2D climate model.

There are several conventions for
spherical coordinates. In the geographic coordinate system, we speak of latitude/colatitude and longitude:

* **Latitude** ($\lat$): North-south direction. Latitude lines are parallel to the equator and are assigned the angle from the equator.
* **Colatitude** ($\colat$): Complementary angle from a given latitude (meassured from the north pole).

| Location   | Latitude| Colatitude|
| -----------|---------|-----------|
| North pole | 90°     | 0°        |
| Equator    | 0°      |90°|
| South pole | -90° | 180°|

* **Longitude** ($\varphi$): East-West direction. Longitude lines are perpendicular to the equator with range West -180° to East +180°.

![](/assets/milestone1/LongLat.png)
* **Source:** Wikipedia.

@@colbox-blue
**Remark 1:** the values of longitude and latitude can be given in radians or degrees.
@@

@@colbox-blue
**Remark 2:** In geography, the generation of a map
with long/lat values of a location always
depends on the choice of a reference system: the
so-called **geodetic datum**. The geodetic datum
is a reference ellipsoid. Only in
combination (map+geodetic datum) the
coordinates are precise and can be compared.
@@

We consider the spherical coordinate system, in which all points in the three-dimensional space can be located using three variables:
* Radius ($r \in \R, \, 0 \le r < \infty$),
* Latitude ($\lat \in \R, \, -\pi/2 \le r < \pi/2$) **or** colatitude ($\colat \in \R, \, 0 \le r < \pi$),
* Longitude: $\varphi \in \R, \, 0 \le r < 2\pi$.

![](/assets/milestone1/SphereCoord.png)

We can map any point in absolute Cartesian coordinates ($x,y,z$) to spherical coordinates ($r,\colat,\varphi$) using the following transformations:
\begin{align}
x &= r \sin \colat \cos \varphi, & r &= \sqrt{x^2 + y^2 + z^2},\\
y &= r \sin \colat \sin \varphi, & \colat &= \arctan \left(\frac{x^2 + y^2}{z} \right),\\
z &= r \cos \colat, & \varphi &= \arctan(y/z).
\end{align}

From mathematical analysis, we know that the Jacobian of the coordinate transformation is given by
\begin{align}
\partialderiv{x}{r} &= \sin \colat \cos \varphi, &
\partialderiv{x}{\varphi} &= -r \sin \colat \sin \varphi, & 
\partialderiv{x}{\colat} &= r \cos \colat \cos \varphi \\
\partialderiv{y}{r} &= \sin \colat \sin \varphi, &
\partialderiv{y}{\varphi} &= r \sin \colat \cos \varphi, & 
\partialderiv{y}{\colat} &= r \cos \colat \sin \varphi \\
\partialderiv{z}{r} &= \sin \colat \cos \colat, &
\partialderiv{z}{\varphi} &= 0, & 
\partialderiv{z}{\colat} &= -r \sin \colat,
\end{align}
and the respective Jacobian matrix,
\begin{align}
J =
\partialderiv{(x,y,z)}{(r,\colat,\varphi)} =
\begin{bmatrix}
\sin \colat \cos \varphi & -r \sin \colat \sin \varphi & r \cos \colat \cos \varphi \\
\sin \colat \sin \varphi & r \sin \colat \cos \varphi & r \cos \colat \sin \varphi \\
\sin \colat \cos \colat  & 0 & -r \sin \colat 
\end{bmatrix}
\in \R^{3 \times 3}
\end{align}
with the determinant
$$\label{eq:det}
|J|=r^2 \sin \colat.
$$

@@colbox-blue
**Example:**  The coordinate transformation can be used to compute the volume of a sphere with radious R:
\begin{align}
\iiint_{V} \d V &= \iiint_{V} \d x \d y \d z \\
&= \int_{r=0}^R \int_{\colat=0}^{\pi} \int_{\varphi=0}^{2\pi} |J| \d r \d \colat \d \varphi\\
&= \frac{4\pi R^3}{3}
\end{align}
@@

## Meshing the sphere

In numerical methods, we often partition the domain in smaller subdomains using what is called a mesh. We will then approximate the solution to the partial differential equation that describes our model within each of those subdomains.

The easiest way to partition a sphere is to use subdomains with uniform radius, latitude/colatitude and longitude spacings:

![](/assets/milestone1/PolesProblem.png)
* **Source**: Wikipedia

We can observe from the figure that the
grid cells get smaller the closer they are to the
poles. So a regular grid in (co-)latitude and
longitude space gives an irregular grid on the
sphere surface.
In fact, we can note that the determinant \eqref{eq:det} can
get equal to zero for $\colat \in \{ 0, \pi\}$. From linear
algebra, we know that matrices with determinant
equal to zero are not regular, i.e., they cannot
be invented. Transformations where the Jacobian
matrix gets irregular are singular at this specific
locations. The locations $\colat=0$ (North) and $\colat=\pi$ (South)
correspond to the poles. Therefore, the transformation is
singular at the poles, which shows that, regarding
mappings, the poles are special locations and
are somewhat problematic when trying to
mesh the surface.


Because of the issues discussed above,
there are many alternative ways of constructing
meshes for sphere:

![](/assets/milestone1/GridsSphere.png)
* **Source**: [https://www.encyclopedie-environnement.org](https://www.encyclopedie-environnement.org)

For instance, the famous ICON (Icosahedral Nonhydrostatic) model from the German weather service (DWD: Deutschen Wetterdienst) uses triangle
surface grids:


![](/assets/milestone1/ICONgrid.png)
* **Source**: [www.dwd.de](http://www.dwd.de)

Although we have identified some issues with grids that are regular in latitude/colatitude and longitude, we have decided to use this type of grid in our model. Despite its limitations, it is the simplest grid to construct and work with. To address the singularities at the poles, we will develop and implement a special fix.

The grid that we use in this course is illustrated below:

![](/assets/milestone1/OurGrid.png)

In the illustration, the boundaries of our domain are marked in blue, the grid lines of the mesh are marked in red and the grid points of the mesh (the positions where we will store our numerical solution) are marked as purple circles.

Since our domain is periodic in the longitude direction, we do not need to store the last column of grid points ($\varphi = \pi$), as their position on the surface of the sphere is the same as for the first column ($\varphi = -\pi$).

Note that all the points in the first row ($\lat = \pi/2$) correspond to the same position (north pole), and all the points in the last row ($\lat = -\pi/2$) too (south pole).
Nevertheless, we will keep these duplicated grid points in our model to simplify the storage (we can use a matrix to store the values).

We define the number of grid points as
\begin{align}
\nlong \in \mathbb{N} \\
\nlat \in \mathbb{N}
\end{align}
to get the size of the grid cells as
\begin{align}
\Delta \varphi &= \frac{2\pi}{\nlong} \\
\Delta \lat &= \Delta \colat = \frac{\pi}{\nlat -1}.
\end{align}

To simplify the derivation of our numerical climate model, we will use uniform grids, i.e., $\Delta \varphi = \Delta \lat$, so we get:
$$
\nlong = 2(\nlat - 1).
$$

The longitude grid node locations are
\begin{align}
\varphi_i &= -\pi + (i-1) \Delta \varphi, & i&=1, 2, \ldots, \nlong,
\end{align}
the latitude grid node locations are
\begin{align}
\lat_j &= -\frac{\pi}{2} + (j-1) \Delta \lat, & j&= 1, 2, \ldots, \nlat,
\end{align}
and equivalently the colatitude grid node locations are
\begin{align}
\colat_j &= (j-1) \Delta \colat, & j&= 1, 2, \ldots, \nlat.
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
transform has no mathematical properties (it does not keep distances, angles, or areas) but
was designed by Robinson by hand to look
pleasing to his eyes(!).

While Robinson provided a translation
table for values (lat/lon), there are
closed form approximations available.
The form we consider was presented by
> Beineke, D. (1991). Untersuchung zur Robinson-Abbildung und Vorschlag einer analytischen Abbildungsvorschrift. Kartographische Nachrichten, 41(3), 85-94.

The approximation that Beineke proposes
is based on a polynomial spline approximation.
Given the computational coordinates, he defines the new coordinates of the
curvilinear grid as
\begin{align}
    \hat{x}_{ij} &= (d + e \lat_j^2 + f \lat_j^4 + g \lat_j^6) \varphi_i \\
    x &= \frac{180}{\pi} \frac{\hat{x}_{ij}}{\max_{i,j} (\hat{x}_{ij})} \\
    \hat{y}_{ij} &= a \lat_j + b \texttt{sign} (\lat_j) |\lat_j|^c \\
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
topic of the first assignment.

