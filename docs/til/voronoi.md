title: Voronoi diagram
tags: data, visualisation, mathematics
author: Colm Britton
source: https://en.wikipedia.org/wiki/Voronoi_diagram
created: 2020/05/14
updated: 2022/08/22
--------------------

A [Voronoi diagram](https://en.wikipedia.org/wiki/Voronoi_diagram) is a diagram where regions are calculated for a given point. Each region is all the points/pixels closer to the point we are interested in than any other. These regions are called Voronoi cells.

![Animated example of voronoi diagram](/static/images/notes/Voronoi_growth_euclidean.gif)

### Examples

* Voronoi diagrams are superimposed on oceanic plot charts so planes know where the nearest airfield is for in-flight diversions
* Use to estimate yields for mining. Drillholes act as the original points.
* For nearest neighbour queries. E.g. find nearest hospital to a given location (pt)
* Can be used to find the biggest possible circle between points or in a polygon. E.g. find point to build supermarket that is furthest from any other
* they can used to calculate hover areas for points on a chart or map. E.g. [ONS scatter charts](https://www.ons.gov.uk/visualisations/dvc806/scatter/scatter/index.html)
* estimating postcode boundaries from point data (we did this in WRA)

### Links

* [d3 plugin](https://github.com/d3/d3-voronoi)

