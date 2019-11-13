from Geometry import *

from math import pi,cos,sin
import numpy

lines=Circle(increment=pi/32,p=-0.9,q=-0.9)
lines.extend(Circle(increment=pi/32,p=0.9,q=-0.9))
lines.extend(Circle(increment=pi/32,p=-0.9,q=0.9))
lines.extend(Circle(increment=pi/32,p=0.9,q=0.9))
#values=EndToEnd(lines,increment=pi/32)
visible=LoadData("visible")
values=Shine(visible)
plot0=Graph()
plot0.Lines(lines)
plot=Graph()
plot.Values(values)
plot.Save("Graph")
Graph.Show()


