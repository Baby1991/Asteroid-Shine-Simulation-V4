from Geometry import *

from math import pi,cos,sin
import numpy as np
import sys

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

path=sys.argv[1]
filename=sys.argv[0]

text=LoadTxt(path+"/"+filename,split1=" ")
points=Points_Coord(text,True)
x,z,y = zip(*points)
points=list(zip(x,y,z))

shine=[]
slices=Slice(points,10)
#print(slices)
for sl in slices:
    ast=Asteroid(phase=pi/9,increment=pi/36,radius=5000,Density=100)
    ast.Lines(Lines_From_Coords(FixPoints(sl)))
    
    ast.Test()
    if not shine:
        shine=ast.shine
    else:
        for i in range(len(ast.shine)):
            shine[i]=shine[i]+ast.shine[i]

plot=Graph()
plot.Values(shine)
plot.Save("shine_"+filename,path=path)
plot=Graph()
plot.Values(Filter(shine))
plot.Save("FilteredShine_"+filename,path=path)