from Geometry import *

from math import pi,cos,sin
import numpy

ref=Point(5,0)

line=Line(Point(-1,0),Point(0,1))
occluder=Line(Point(1,-1),Point(0,0))
plot=Graph()
plot.Line(line)
plot.Line(occluder)
plot.Point(ref)
out=line.Visibility(occluder,ref)
if out:
    plot.Lines(out,color="red")
Graph.Show()
