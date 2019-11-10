from Geometry import *

from math import pi,cos,sin
import numpy

ref=Point(5,0)



lines=Circle(increment=pi/2)

visible=Visible_Lines_From_Point(lines,ref)

plot=Graph()
plot.Lines(lines)
plot.Lines(visible,color="red")

Graph.Show()
