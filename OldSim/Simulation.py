from Geometry import *

from math import pi,cos,sin

#lines=Circle(increment=pi/32)
lines=Circle(increment=pi/32,p=-0.9,q=-0.9)
lines.extend(Circle(increment=pi/32,p=0.9,q=-0.9))
lines.extend(Circle(increment=pi/32,p=-0.9,q=0.9))
lines.extend(Circle(increment=pi/32,p=0.9,q=0.9))

visible=Test_Lines(lines,increment=pi/2,phase=0)

for i,j,k in visible:
    plot=Graph()
    plot.Lines(lines,linewidth=5)
    plot.Lines(i,color="red")
    Graph.Show()

    

