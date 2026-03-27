+++
title = "General Information"
hascode = true
date = Date(2019, 3, 22)
rss = "Description"

rss_title = "0 General Info"

tags = ["syntax", "code"]
+++

# General Information

\toc

## Goals for this Course

* Implement your own (simple) climate model from scratch. We teach you everything(!) that is necessary.
* Get an idea about climate physics.
* Get an idea how to describe the physics with ODEs and PDEs.
* Learn how to numerically solve ODEs and PDEs.
* Learn how to implement the numerical algorithms.
* Learn how to set up simple climate simulations.
* Learn how to discuss the results and understand the limitations of the modeling.
* Use everything learned to extend the model.

## Structure of the Course
* We have 6 pre-made milestones (sub-projects) with the following structure:
  1. "Theory phase": Lectures that provide all theoretical information necessary to reach the milestone.
  2. "Implementation phase": Hands-on programming in groups. We are here to help: can be used to sit together and work on the milestones, ask questions, discussions, etc.
* In the final part of the lecture, there will be the mysterious milestone 7.
* For the milestones 1-6 solutions in Julia and Python are available and made accessible.
* Below you can find the schedule.

~~~
<style>
  body {
    margin: 2cm;
    margin-top: 1cm;
    margin-bottom: 1cm;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    border-top: 2px solid black;
    border-bottom: 2px solid black;
  }

  thead th {
    border-bottom: 1px solid black;
    padding: 6px 8px;
    text-align: left;
    font-weight: normal;
  }

  th.center, td.center {
    text-align: center;
  }

  td {
    padding: 4px 8px;
    vertical-align: top;
  }

  /* Week column colors */
  .weekA { background-color: #f2f2f2; } /* gray 95% */
  .weekB { background-color: #e6e6e6; } /* gray 90% */

  /* Activity colors */
  .lecture       { background-color: #FFE0B2; }
  .handson       { background-color: #C8E6C9; }
  .presentation  { background-color: #E1BEE7; }

  /* Milestone separator: border-top on cols 2-5, not col 1 */
  tr.ms-sep td:nth-child(n+2) {
    border-top: 1px solid #aaa;
  }

  /* Column spacing */
  td:nth-child(1) { width: 3em; }
  td:nth-child(2), th:nth-child(2) { width: 5em; }
  td:nth-child(4), th:nth-child(4) { width: 3em; }

  .legend {
    margin-top: 8px;
    font-size: 0.9em;
  }
</style>

<table>
<thead>
<tr>
  <th>Week</th>
  <th class="center">Milestone</th>
  <th class="center">Date</th>
  <th class="center">Room</th>
  <th>Activity</th>
</tr>
</thead>
<tbody>
<tr>
  <td class="weekA">1</td>
  <td class="center">1</td>
  <td class="center">15.04.2026, 12:00</td>
  <td class="center">HS</td>
  <td class="lecture">Lecture</td>
</tr>
<tr>
  <td class="weekA"></td>
  <td class="center"></td>
  <td class="center">15.04.2026, 14:00</td>
  <td class="center">CV</td>
  <td class="lecture">Lecture</td>
</tr>
<tr>
  <td class="weekA"></td>
  <td class="center"></td>
  <td class="center">16.04.2026, 12:00</td>
  <td class="center">HS</td>
  <td class="handson">Hands-on</td>
</tr>
<tr>
  <td class="weekB">2</td>
  <td class="center"></td>
  <td class="center">22.04.2026, 12:00</td>
  <td class="center">HS</td>
  <td class="handson">Hands-on</td>
</tr>
<tr class="ms-sep">
  <td class="weekB"></td>
  <td class="center">2</td>
  <td class="center">22.04.2026, 14:00</td>
  <td class="center">CV</td>
  <td class="lecture">Lecture</td>
</tr>
<tr>
  <td class="weekB"></td>
  <td class="center"></td>
  <td class="center">23.04.2026, 12:00</td>
  <td class="center">HS</td>
  <td class="lecture">Lecture</td>
</tr>
<tr>
  <td class="weekA">3</td>
  <td class="center"></td>
  <td class="center">29.04.2026, 12:00</td>
  <td class="center">HS</td>
  <td class="lecture">Lecture</td>
</tr>
<tr>
  <td class="weekA"></td>
  <td class="center"></td>
  <td class="center">29.04.2026, 14:00</td>
  <td class="center">CV</td>
  <td class="handson">Hands-on</td>
</tr>
<tr>
  <td class="weekA"></td>
  <td class="center"></td>
  <td class="center">30.04.2026, 12:00</td>
  <td class="center">HS</td>
  <td class="handson">Hands-on</td>
</tr>
<tr>
  <td class="weekB">4</td>
  <td class="center"></td>
  <td class="center">06.05.2026, 12:00</td>
  <td class="center">HS</td>
  <td class="handson">Hands-on</td>
</tr>
<tr class="ms-sep">
  <td class="weekB"></td>
  <td class="center">3</td>
  <td class="center">06.05.2026, 14:00</td>
  <td class="center">CV</td>
  <td class="lecture">Lecture</td>
</tr>
<tr>
  <td class="weekB"></td>
  <td class="center"></td>
  <td class="center">07.05.2026, 12:00</td>
  <td class="center">HS</td>
  <td class="lecture">Lecture</td>
</tr>
<tr>
  <td class="weekA">5</td>
  <td class="center"></td>
  <td class="center">13.05.2026, 12:00</td>
  <td class="center">HS</td>
  <td class="handson">Hands-on</td>
</tr>
<tr>
  <td class="weekA"></td>
  <td class="center"></td>
  <td class="center">13.05.2026, 14:00</td>
  <td class="center">CV</td>
  <td class="handson">Hands-on</td>
</tr>
<tr class="ms-sep">
  <td class="weekB">6</td>
  <td class="center">4</td>
  <td class="center">20.05.2026, 12:00</td>
  <td class="center">HS</td>
  <td class="lecture">Lecture</td>
</tr>
<tr>
  <td class="weekB"></td>
  <td class="center"></td>
  <td class="center">20.05.2026, 14:00</td>
  <td class="center">CV</td>
  <td class="handson">Hands-on</td>
</tr>
<tr>
  <td class="weekB"></td>
  <td class="center"></td>
  <td class="center">21.05.2026, 12:00</td>
  <td class="center">HS</td>
  <td class="handson">Hands-on</td>
</tr>
<tr class="ms-sep">
  <td class="weekA">8</td>
  <td class="center">5</td>
  <td class="center">03.06.2026, 12:00</td>
  <td class="center">HS</td>
  <td class="lecture">Lecture</td>
</tr>
<tr>
  <td class="weekA"></td>
  <td class="center"></td>
  <td class="center">03.06.2026, 14:00</td>
  <td class="center">CV</td>
  <td class="lecture">Lecture</td>
</tr>
<tr>
  <td class="weekB">9</td>
  <td class="center"></td>
  <td class="center">10.06.2026, 12:00</td>
  <td class="center">HS</td>
  <td class="handson">Hands-on</td>
</tr>
<tr>
  <td class="weekB"></td>
  <td class="center"></td>
  <td class="center">10.06.2026, 14:00</td>
  <td class="center">CV</td>
  <td class="handson">Hands-on</td>
</tr>
<tr>
  <td class="weekB"></td>
  <td class="center"></td>
  <td class="center">11.06.2026, 12:00</td>
  <td class="center">HS</td>
  <td class="handson">Hands-on</td>
</tr>
<tr>
  <td class="weekA">10</td>
  <td class="center"></td>
  <td class="center">17.06.2026, 12:00</td>
  <td class="center">HS</td>
  <td class="handson">Hands-on</td>
</tr>
<tr class="ms-sep">
  <td class="weekA"></td>
  <td class="center">6</td>
  <td class="center">17.06.2026, 14:00</td>
  <td class="center">CV</td>
  <td class="lecture">Lecture</td>
</tr>
<tr>
  <td class="weekA"></td>
  <td class="center"></td>
  <td class="center">18.06.2026, 12:00</td>
  <td class="center">HS</td>
  <td class="handson">Hands-on</td>
</tr>
<tr>
  <td class="weekB">11</td>
  <td class="center"></td>
  <td class="center">24.06.2026, 12:00</td>
  <td class="center">HS</td>
  <td class="handson">Hands-on</td>
</tr>
<tr>
  <td class="weekB"></td>
  <td class="center"></td>
  <td class="center">24.06.2026, 14:00</td>
  <td class="center">CV</td>
  <td class="handson">Hands-on</td>
</tr>
<tr class="ms-sep">
  <td class="weekB"></td>
  <td class="center">7</td>
  <td class="center">25.06.2026, 12:00</td>
  <td class="center">HS</td>
  <td class="lecture">Lecture</td>
</tr>
<tr>
  <td class="weekA">12</td>
  <td class="center"></td>
  <td class="center">01.07.2026, 12:00</td>
  <td class="center">HS</td>
  <td class="lecture">Lecture</td>
</tr>
<tr>
  <td class="weekA"></td>
  <td class="center"></td>
  <td class="center">01.07.2026, 14:00</td>
  <td class="center">CV</td>
  <td class="lecture">Lecture/Hands-on</td>
</tr>
<tr>
  <td class="weekA"></td>
  <td class="center"></td>
  <td class="center">02.07.2026, 12:00</td>
  <td class="center">HS</td>
  <td class="handson">Hands-on</td>
</tr>
<tr>
  <td class="weekB">13</td>
  <td class="center"></td>
  <td class="center">08.07.2026, 12:00</td>
  <td class="center">HS</td>
  <td class="handson">Hands-on</td>
</tr>
<tr>
  <td class="weekB"></td>
  <td class="center"></td>
  <td class="center">08.07.2026, 14:00</td>
  <td class="center">CV</td>
  <td class="handson">Hands-on</td>
</tr>
<tr>
  <td class="weekB"></td>
  <td class="center"></td>
  <td class="center">09.07.2026, 12:00</td>
  <td class="center">HS</td>
  <td class="handson">Hands-on</td>
</tr>
<tr>
  <td class="weekA">14</td>
  <td class="center"></td>
  <td class="center">15.07.2026, 12:00</td>
  <td class="center">HS</td>
  <td class="handson">Hands-on</td>
</tr>
<tr>
  <td class="weekA"></td>
  <td class="center"></td>
  <td class="center">15.07.2026, 14:00</td>
  <td class="center">CV</td>
  <td class="handson">Hands-on</td>
</tr>
<tr>
  <td class="weekA"></td>
  <td class="center"></td>
  <td class="center">16.07.2026, 12:00</td>
  <td class="center">HS</td>
  <td class="presentation">Presentations</td>
</tr>
<tr>
  <td class="weekB">15</td>
  <td class="center"></td>
  <td class="center">22.07.2026, 12:00</td>
  <td class="center">HS</td>
  <td class="presentation">Presentations</td>
</tr>
<tr>
  <td class="weekB"></td>
  <td class="center"></td>
  <td class="center">23.07.2026, 12:00</td>
  <td class="center">HS</td>
  <td class="presentation">Presentations</td>
</tr>
</tbody>
</table>
~~~
HS = Hörsaal des Mathematischen Instituts (Raum 203) \
CV = Cohn-Vossen-Raum (Raum 313)

## Examination

* Milestone 1-6 are not graded. Their purpose is to learn the climate model and prepare for milestone 7.
* Milestone 7 is free style and the topic chosen by students with a final (Jupyter/Pluto notebook) presentation at the end of the semester that will be graded (pass/fail). Again, we are here to help: we will guide and supervise the selection of topics for milestone 7, and give advice and support during the hands-on phase.
* Admission criterion for oral exam: Pass milestone 7.
* Per person oral exam (most likely in the first week of August).
<!-- (10 - 15 minutes) -->

## Organization of the course

* All announcements and internal communications will be done via [ILIAS](https://www.ilias.uni-koeln.de/ilias/goto_uk_crs_6744928.html)!
* Make sure that you can log in there and check "general information".
* If you have a question, please post in [ILIAS questions/comments section](https://www.ilias.uni-koeln.de/ilias/goto_uk_frm_6778388.html).
