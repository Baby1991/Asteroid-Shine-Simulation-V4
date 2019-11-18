from Geometry import *

from math import pi,cos,sin
import numpy as np

ast=Asteroid("Asteroid 1",increment=pi/2,phase=0)

ast.Ellipse(increment=pi/8,p=-0.9)
ast.Ellipse(increment=pi/8,p=0.9)
ast.Ellipse(increment=pi/8,q=-0.9)
ast.Ellipse(increment=pi/8 ,q=0.9)

#ast.Load("Asteroid 512 512 1024")

ast.Test()
ast.Save()
#Shutdown()

#ast.Plot().Save(ast.name)
plot=Graph()
plot.Lines(ast.lines,linewidth=7)
i=0
for r in ast.visible[0][0]:
    plot.Line(r,color="red")
    plot.Save(str(i))
    plot.Line(r,color="blue",linewidth=7)
    i+=1