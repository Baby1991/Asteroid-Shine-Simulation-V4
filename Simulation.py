from Geometry import *

from math import pi,cos,sin
import numpy as np
import sys,os

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

path=os.path.join(os.getcwd(),sys.argv[1])
name=sys.argv[2]

shine=Test_Object(name,path,10)

SaveData(shine,"shine",path)

"""shine=LoadData(name,path)
plot=Graph()
plot.Values(shine)
plot.Save("shine",path)
plot=Graph()
plot.Values(Filter(shine))
plot.Save("filtered",path)"""