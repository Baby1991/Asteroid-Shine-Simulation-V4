from Geometry import *

from math import pi,cos,sin
import numpy as np
import sys,os

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

savepath0=os.path.join(os.getcwd(),sys.argv[1])
filename0=sys.argv[2]

trigs=LoadTriangles(os.path.join(savepath0,filename0))
shine=[]
slices=Slice(trigs,100)

for sl in slices:
    ast=Asteroid(phase=pi/9,increment=pi/36,radius=5000,Density=100)
    ast.Lines(sl)
    ast.Test()
    if not shine:
        shine=ast.shine
    else:
        for i in range(len(ast.shine)):
            shine[i]=shine[i]+ast.shine[i]

SaveData(shine,"shine",savepath0)

