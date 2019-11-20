from Geometry import *

from math import pi,cos,sin
import numpy as np
import random

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""ast=Asteroid(phase=0,increment=pi/16,radius=100,Density=1000)
ast.Ellipse(a=50,b=50,increment=pi/64)
ast.Test(1)
plot=Graph()
plot.Values(ast.shine)
Graph.Show()
exit()"""

text=LoadTxt("Cilindar/Cilindar.xyz",split1=" ")
points=Points_Coord(text,True)
x,z,y = zip(*points)
points=list(zip(x,y,z))

fig=plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x,y,z)
plt.savefig("Object")

shine=[]
slices=Slice(points,7)
#print(slices)
j=0
for sl in slices:
    print(j)
    ast=Asteroid(phase=pi/18,increment=pi/64,radius=1000,Density=100)
    ast.Lines(Lines_From_Coords(FixPoints(sl)))
    plot=Graph()
    plot.Lines(Lines_From_Coords(FixPoints(sl)))
    Graph.Show()
    
    """ast.Test()
    if not shine:
        shine=ast.shine
    else:
        for i in range(len(ast.shine)):
            shine[i]=shine[i]+ast.shine[i]

    j+=1


plot=Graph()
plot.Values(shine)
plot.Save("shine")
plot=Graph()
plot.Values(Filter(shine))
plot.Save("FilteredShine")"""