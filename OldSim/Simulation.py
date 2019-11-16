from Geometry import *

from math import pi,cos,sin

ast=Asteroid()
"""ast.Circle(increment=pi/256,p=-0.9,q=-0.9)
ast.Circle(increment=pi/256,p=0.9,q=-0.9)
ast.Circle(increment=pi/256,p=-0.9,q=0.9)
ast.Circle(increment=pi/256,p=0.9,q=0.9)
ast.Test_Shine(phase=0,increment=pi/512)"""

ast.Load("Asteroid")
#ast.Test_Shine()
#ast.Save()

plot=Graph()
plot.Values(ast.shine)
plot.Save("Shine")
Graph.Show()