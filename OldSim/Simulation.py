from Geometry import *

from math import pi,cos,sin
import numpy as np

ast=Asteroid("Asteroid 1",increment=pi,phase=0,radius=5)

ast.Ellipse(increment=pi/16,p=-0.7)
ast.Ellipse(increment=pi/16,p=0.7)
ast.Ellipse(increment=pi/16,q=-0.7)
ast.Ellipse(increment=pi/16,q=0.7)

#ast.Load("Asteroid 512 512 1024")
#ast.Plot().Save(ast.name)
ast.Test()
ast.Save()
#Shutdown()
plot=Graph()
x,y,z=ast.visible[0]
i=0
plot.Lines(x,linewidth=5)
for line in x:

    plot.Line(line,color="red")
    plot.Save(str(i))
    i+=1

