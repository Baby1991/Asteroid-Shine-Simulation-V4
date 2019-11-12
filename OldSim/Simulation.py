from Geometry import *

from math import pi,cos,sin
import numpy

lines=Circle(increment=pi/128,p=-1)
lines.extend(Circle(increment=pi/128,p=1))



EndToEnd(lines,increment=pi/128,Density=100)
