from Geometry import *

from math import pi,cos,sin
import numpy as np
import sys,os

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

path=os.path.join(os.getcwd(),sys.argv[1])
name=sys.argv[2]

ast=Asteroid(name,path)
shine=ast.Test_Object(1)
SaveData(shine,name,path)
