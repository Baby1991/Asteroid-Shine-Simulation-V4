from Geometry import *

from math import pi,cos,sin
import numpy

ref=Point(5,0)
#lines=[Line(Point(1,-2),Point(1,-1)),Line(Point(1,1),Point(1,2)),Line(Point(0,5),Point(0,-5)),Line(Point(-1,-5),Point(-1,5))]

#lines=[Line(Point(1,1),Point(1,2)),Line(Point(1,-3),Point(1,-2)),Line(Point(1,0),Point(1,1)),Line(Point(0,5),Point(0,-5)),Line(Point(-1,-5),Point(-1,5)),Line(Point(-2,-5),Point(-2,5))]


#line=Line(Point(-3,5),Point(-3,-5))
lines=[Line(Point(1,-2),Point(1,-1)),Line(Point(1,1),Point(1,2)),Line(Point(0,5),Point(0,2)),Line(Point(0,-5),Point(0,-2)),Line(Point(0,-1.5),Point(0,1.5)),Line(Point(-1,5),Point(-1,-5)),Line(Point(-2,5),Point(-2,-5))]

visible=Visible_Lines_From_Point(lines,ref)
#visible=line.vs_Sect(lines,ref)

plot=Graph()
plot.Lines(lines,linewidth=6)
#plot.Line(line,color="blue")
if visible:
    plot.Lines(visible,color="red",marker=".",linewidth=3)
plot.Point(ref)
Graph.Show()
