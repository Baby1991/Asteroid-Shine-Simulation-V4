
from Geometry import *

from math import pi,cos,sin
import numpy

lines=Circle(start=0,end=2*pi,increment=pi/4)

for i in numpy.arange(0,2*pi,pi/4):
    ref=Point(5*cos(i),5*sin(i))
    plot1=Graph()
    plot1.Lines(Visible_Lines_From_Point(lines,ref))
    plot1.Point(ref)
    Graph.Show()










