
from Geometry import *


linije=[]
step=pi/10
ref=Point(10,0)

refl=Line(ref,ref)

lines=Circle(start=0,end=2*pi,increment=pi/16)

plot=Visible_Lines_From_Point(lines,ref)
plot.append(refl)
plot1=lines
plot1.append(refl)

Graph(plot)
Graph(plot1)

