
from Geometry import *

from math import pi,cos,sin
linije=[]
step=pi/10
ref=Point(2,0)
"""
for i in range(5,15,1):
    t0=i*step
    t=(i+1)*step
    pp=Point(round(cos(t0),10),round(sin(t0),10))
    p=Point(round(cos(t),10),round(sin(t),10))
    l=Line(pp,p)
    linije.append(l)
print(linije)
print("\n")

sectors=linije
"""
l1=Line(Point(-2,2),Point(-2,-2))
l2=Line(Point(0,2),Point(0,0))
print(l1.Visibility(l2,ref))

