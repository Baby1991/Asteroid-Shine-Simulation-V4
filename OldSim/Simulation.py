from Geometry import *

from math import pi,cos,sin
import numpy as np

ast=Asteroid("Asteroid 1",increment=pi/128,phase=0)

ast.Ellipse(increment=ast.increment,p=-1)
ast.Ellipse(increment=ast.increment,p=1)
ast.Ellipse(increment=ast.increment,q=-1)
ast.Ellipse(increment=ast.increment,q=1)
#ast.Ellipse(increment=ast.increment)
#ast.Load("Asteroid 1")

ast.Test(1)
#ast.Load("Asteroid 1")

#Shutdown()

#ast.FixLines(increment=ast.increment)
#print(len(ast.fixedLines))
#print(len(ast.lines))
#print(len(ast.fixedLines))


#ast.Save()

"""plot=Graph()
plot.Lines(ast.lines,linewidth=5)
plot.Lines(ast.fixedLines,color="red")
Graph.Show()"""
#ast.Plot().Save(ast.name)
#ast.shine.append(1)
plot=Graph()
plot.Values(ast.shine)
Graph.Show()

"""for x,y,z in ast.visible:
    print(len(x))"""
    