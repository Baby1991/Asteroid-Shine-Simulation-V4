from Geometry import *

from math import pi,cos,sin
import numpy as np
import sys,os



import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

savepath0=os.getcwd()+"\\"+sys.argv[1]
filename0=sys.argv[2]

text=LoadTxt(savepath0+"\\"+filename0+".xyz",split1=" ")
points=Points_Coord(text,True)
x,z,y = zip(*points)
points=list(zip(x,y,z))

shine=[]
slices=Slice(points,10)
#print(slices)
for sl in slices:
    ast=Asteroid(phase=pi/9,increment=pi/36,radius=5000,Density=100)
    ast.Lines(Lines_From_Coords(FixPoints(sl),n=7))
    
    ast.Test()
    if not shine:
        shine=ast.shine
    else:
        for i in range(len(ast.shine)):
            shine[i]=shine[i]+ast.shine[i]

plot=Graph()
plot.Values(shine)
plot.Save("shine_"+filename0,path=savepath0)
plot=Graph()
plot.Values(Filter(shine))
plot.Save("FilteredShine_"+filename0,path=savepath0)