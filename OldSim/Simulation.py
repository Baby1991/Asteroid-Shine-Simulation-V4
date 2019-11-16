from Geometry import *

from math import pi,cos,sin

ast=Asteroid()
ast.Circle(increment=pi/32,p=-0.9,q=-0.9)
ast.Circle(increment=pi/32,p=0.9,q=-0.9)
ast.Circle(increment=pi/32,p=-0.9,q=0.9)
ast.Circle(increment=pi/32,p=0.9,q=0.9)
#ast.Load(lines="lines")
ast.Test_Shine(phase=0,increment=pi/32)
val=[]
for t,_,_ in ast.visible:
    val.append(len(t))
plot=Graph()
plot.Values(val)
plot.Save("Graph")

ast.Save(visible="visible",shine="shine")
plot=Graph()
plot.Values(ast.shine)
Graph.Show()
ast.Plot().Save(ast.name)

    
