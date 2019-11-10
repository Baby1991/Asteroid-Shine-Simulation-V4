from Geometry import *

from math import pi,cos,sin
import numpy

ref=Point(5,0)

lines=Circle(increment=pi/8)

visible=Visible_Lines_From_Point(lines,ref)

plot=Graph()
plot.Lines(lines,linewidth=6)
if visible:
    plot.Lines(visible,color="red",marker=".",linewidth=3)
plot.Point(ref)
Graph.Show()
