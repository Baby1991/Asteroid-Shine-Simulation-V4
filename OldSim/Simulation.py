from Geometry import *

from math import pi,cos,sin

ast=Asteroid()
"""ast.Circle(increment=pi/128,p=-0.9,q=-0.9)
ast.Circle(increment=pi/128,p=0.9,q=-0.9)
ast.Circle(increment=pi/128,p=-0.9,q=0.9)
ast.Circle(increment=pi/128,p=0.9,q=0.9)
ast.Test_Shine(phase=0,increment=pi/256)
ast.Save(name=ast.name)
plot=Graph()
plot.Values(ast.shine)
Graph.Show()
ast.Plot().Save(ast.name)"""
ast.Load(fixedLines="fixedLines")
ast.Test_Shine(increment=pi/32)
plot=Graph()
plot.Values(Filter(ast.shine,150))
plot.Save("Filtered")
Graph.Show()
    
