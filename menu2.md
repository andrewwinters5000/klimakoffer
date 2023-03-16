+++
title = "Milestone 1"
hascode = true
rss = "A short description of the page which would serve as **blurb** in a `RSS` feed; you can use basic markdown here but the whole description string must be a single line (not a multiline string). Like this one for instance. Keep in mind that styling is minimal in RSS so for instance don't expect maths or fancy styling to work; images should be ok though: ![](https://upload.wikimedia.org/wikipedia/en/b/b0/Rick_and_Morty_characters.jpg)"
rss_title = "Milestone 1"
rss_pubdate = Date(2019, 5, 1)

tags = ["syntax", "code", "image"]
+++

# Milestone 1
\toc

## Introduction Components of the Climate System

![](/_figs/milestone1/ClimateSystem.png)
* Figure from lecture notes: [Stocker, "Introduction to Climate Modeling". Universität Bern](https://climatehomes.unibe.ch/~stocker/papers/stocker18icm.pdf).

### Atmosphere

Gasous part above the Earth's surface. The
atmosphere includes different substances in gaseous (e.g.
CO2), liquid (water, aerosols) or solid (dust) form.

Important processes are for instance:
* Weather 
* Radiation balance: incoming solar radiation, reflection (Albedo), Earth radiation, ...
* Formation of clouds and precipitation
* Turbulent atmospheric flow and heat transfer/mixing

### Hydrosphere 
All forms of water above and below the Earth's surface This includes the whole global water cycle after precipitation has reached the surface


Important processes are for instance:

* Transport of ocean water masses, transport of heat.
* Change of inflow into different ocean basins.
* Connection between oceans and atmosphere., e.g. exchange of water vapour.
* Most important reservoir for carbon: oceans absorb a large amount of CO2: more than atmosphere and terrestial biosphere (plants and animals) combined.

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

![](/_figs/milestone1/Models.png)
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



@@colbox-blue
**Remark 2:** Geography the generation of a mop
with long that venues of a location always
depends on the choice of a referencesystem the
so called geodetic datum The geodetic datum
basically recreance ellipsoid Only in
combination map geodetic datum the
coordinates make sense and are comparable
@@

We con side real Cartesian Gotye has bagtalk
Map geodeticoffend xyopeknotes are precise and
cededGeeperspeedrical coordinates
radius re R O E r c 00
colatitude o eR O E O C IT
longitude Ye R O S o c 21T
with transformations

\begin{align}
x &= r \sin \theta \cos \varphi, & r &= \sqrt{x^2 + y^2 + z^2},\\
y &= r \sin \theta \sin \varphi, & \theta &= \arctan \left(\frac{x^2 + y^2}{z} \right),\\
z &= r \cos \theta, & \varphi &= \arctan(y/z).
\end{align}
