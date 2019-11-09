from Geometry import *

from math import pi,cos,sin
import numpy

ref=Point(5,0)
occluder=Line(Point(0,5),Point(0,3))
linija=Line(Point(-2,2),Point(-2,-2))

plot=Graph()
plot.Line(linija,color="red",marker="o")
visible=linija.Visibility(occluder,ref)
if visible:
    plot.Lines(visible,color="blue")
plot.Line(occluder)
plot.Point(ref)
Graph.Show()