from Geometry import *

from math import pi,cos,sin
import numpy

lines=Circle(increment=pi/32)

for t in numpy.arange(0,2*pi,pi/2):
    ref=Point(5*cos(t),5*sin(t))

    visible=Visible_Lines_From_Point(lines,ref)

    plot=Graph(abs(5*cos(t))+3,abs(5*sin(t))+3)
    plot.Lines(lines,linewidth=5)
    plot.Lines(visible,color="red")
    plot.Point(ref)

    Graph.Show()


