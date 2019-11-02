
from Geometry import *


linije=[]
step=pi/10
ref=Point(10,0)

refl=Line(ref,ref)

lines=Circle(start=-pi/2,end=pi/2,increment=pi/4)

plot=Visible_Lines_From_Point(lines,ref)
plot.append(refl)
Graph(plot)

