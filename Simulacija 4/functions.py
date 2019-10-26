
from Geometry import Line
from Geometry import Point
from Geometry import Connect_Lines

import math
linije=[]
p=Point(1,0)
ref=Point(2,0)
for i in range(0,11,1):
    t=i*math.pi/10
    pp=p
    p=Point(round(math.cos(t),10),round(math.sin(t),10))
    l=Line(pp,p)
    linije.append(l)
print(linije)
print("\n")
ref.Sort_Lines_By_Distance(linije)
linije=Connect_Lines(linije)
print(linije)

