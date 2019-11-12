from Geometry import *

from math import pi,cos,sin
import numpy

lines=Circle(increment=pi/32,p=-0.5)
#lines.extend(Circle(increment=pi/128,p=0.5))
#EndToEnd(lines,increment=pi/32,Density=100)

visible=Visible_Lines_From_Point(lines,Point(5,0))


    

"""
plot=Graph()
plot.Values(Shine(visible))
Graph.Show()"""
