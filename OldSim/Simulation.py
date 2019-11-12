from Geometry import *

from math import pi,cos,sin
import numpy

#lines=Circle(increment=pi/128,p=-0.5)
#lines.extend(Circle(increment=pi/128,p=0.5))
#EndToEnd(lines,increment=pi/32,Density=100)

visible=LoadData("visible")
plot=Graph()
plot.Values(Shine(visible))
Graph.Show()
