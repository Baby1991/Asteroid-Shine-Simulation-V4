from Geometry import *

from math import pi,cos,sin

lines=Circle(increment=pi/32,p=-0.9,q=-0.9)
lines.extend(Circle(increment=pi/32,p=0.9,q=-0.9))
lines.extend(Circle(increment=pi/32,p=-0.9,q=0.9))
lines.extend(Circle(increment=pi/32,p=0.9,q=0.9))

visible=Test_Lines(lines,increment=pi/4)

values=Shine(visible)

plot=Graph()
plot.Values(values)
plot.Save("Graph")
    

