from Geometry import *

from math import pi,cos,sin
import numpy as np

ast=Asteroid("Asteroid 1",increment=pi/16,phase=0)

ast.Ellipse(increment=pi/16,p=-0.9,q=-0.9)
ast.Ellipse(increment=pi/16,p=0.9,q=-0.9)
ast.Ellipse(increment=pi/16,p=-0.9,q=0.9)
ast.Ellipse(increment=pi/16 ,p=0.9,q=0.9)

#ast.Load("Asteroid 512 512 1024")

ast.Test()
ast.Save()
#Shutdown()

plot=Graph()
r=[len(x) for x,y,z in ast.visible]
plot.Values(r)
plot=Graph()
plot.Values(Filter(r))
Graph.Show()
    