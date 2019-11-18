from Geometry import *

from math import pi,cos,sin
import numpy as np

ast=Asteroid("Asteroid 1",increment=pi/128,phase=0)

ast.Ellipse(increment=pi/32,p=-1)
ast.Ellipse(increment=pi/32,p=1)
ast.Ellipse(increment=pi/32,q=-1)
ast.Ellipse(increment=pi/32 ,q=1)

#ast.Load("Asteroid 512 512 1024")

#ast.Test()
#ast.Load("Asteroid 1")

#Shutdown()

ast.FixLines()
print(len(ast.fixedLines))
#print(len(ast.lines))
#print(len(ast.fixedLines))
#ast.Save()

plot=Graph()
plot.Lines(ast.fixedLines)
Graph.Show()

#ast.Plot().Save(ast.name)

"""plot=Graph()
plot.Values(ast.shine)
Graph.Show()"""

"""for x,y,z in ast.visible:
    print(len(x))"""
    