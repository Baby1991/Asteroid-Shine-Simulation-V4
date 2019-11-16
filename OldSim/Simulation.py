from Geometry import *

from math import pi,cos,sin
import numpy as np

ast=Asteroid()
"""ast.Circle(increment=pi/16,p=-0.9,q=-0.9)
ast.Circle(increment=pi/16,p=0.9,q=-0.9)
ast.Circle(increment=pi/16,p=-0.9,q=0.9)
ast.Circle(increment=pi/16,p=0.9,q=0.9)"""
ast.Function("t","sin(t)")
ast.Plot()
Graph.Show()
#ast.visible=ast.Multi_Thread_Visibility()
#ast.Test_Shine()




#ast.Load("Asteroid")
#ast.Test_Shine()
#ast.Save()

"""ast.Plot().Save("Asteroid")

x=np.arange(0,2,1/512)

plot=Graph()
plot.Values(ast.shine,x)
plot.Save("Shine")
plot=Graph()
plot.Values(Filter(ast.shine),x)
plot.Save("FilteredShine")
Graph.Show()

ast.Save()"""