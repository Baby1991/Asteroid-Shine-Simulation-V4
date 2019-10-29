
from Geometry import Line
from Geometry import Point
from Geometry import Connect_Lines

import math
linije=[]
step=math.pi/10
ref=Point(2,0)
for i in range(5,15,1):
    t0=i*step
    t=(i+1)*step
    pp=Point(round(math.cos(t0),10),round(math.sin(t0),10))
    p=Point(round(math.cos(t),10),round(math.sin(t),10))
    l=Line(pp,p)
    linije.append(l)
print(linije)
print("\n")
ref.Sort_Lines_By_Distance(linije)
linije=Connect_Lines(linije)
print(linije)

