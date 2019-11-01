
from Geometry import *


linije=[]
step=pi/10
ref=Point(2,0)

sect=Circle(start=-pi/2,end=pi/2,increment=pi/2)

l1=Line(Point(-1,2),Point(-1,-2))
l2=Line(Point(0,2),Point(0,-2))

lines=l1.vs_Sect(sect,ref)
print(lines)
Graph(lines)
