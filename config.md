<!--
Add here global page variables to use throughout your website.
-->
+++
author = "Gregor Gassner and Andres Rueda-Ramirez"
mintoclevel = 2

# Add here files or directories that should be ignored by Franklin, otherwise
# these files might be copied and, if markdown, processed by Franklin which
# you might not want. Indicate directories by ending the name with a `/`.
# Base files such as LICENSE.md and README.md are ignored by default.
ignore = ["node_modules/"]

# RSS (the website_{title, descr, url} must be defined to get RSS)
generate_rss = true
website_title = "Franklin Template"
website_descr = "Example website using Franklin"
website_url   = "https://tlienart.github.io/FranklinTemplates.jl/"
+++

<!--
Add here global latex commands to use throughout your pages.
-->
\newcommand{\R}{\mathbb R}
\newcommand{\d}{\mathrm{d}}
\newcommand{\scal}[1]{\langle #1 \rangle}
\newcommand{\partialderiv}[2]{ \frac{\partial {#1}}{\partial {#2} } }

<!-- Name of repository for GitHub pages -->
@def prepath = "IntroToClimateModeling"
