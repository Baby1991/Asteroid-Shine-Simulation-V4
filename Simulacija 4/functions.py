
from Geometry import *


linije=[]
step=pi/10
ref=Point(0,2)
refl=Line(ref,ref)

lines=Circle(start=0,end=2*pi,increment=pi/2)
plot=Visible_Lines_From_Point(lines,ref)
plot.append(refl)
Graph(plot)



