
from Geometry import Line
from Geometry import Point

import math
linije=[]
p=Point(0,0)
ref=Point(2,0)
for i in range(0,21,1):
    t=i*math.pi/10
    pp=p
    p=Point(round(math.cos(t),2),round(math.sin(t),2))
    l=Line(pp,p)
    linije.append(l)



