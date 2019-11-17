from Geometry import *

from math import pi,cos,sin
import numpy as np

ast=Asteroid()
ast.Ellipse(increment=pi/512,p=-0.4,a=0.5,b=0.5)
ast.Ellipse(increment=pi/512,p=0.9)



#ast.Load("Asteroid")
ast.Test_Shine(phase=pi/4,increment=pi/1024,radius=10)
ast.Save()

#ast.Plot().Save("Asteroid")

"""x=np.arange(0,2,1/512)

plot=Graph()
plot.Values(ast.shine,x)
plot.Save("Shine")
plot=Graph()
plot.Values(Filter(ast.shine)[0],x)
plot.Save("LowPass")
plot=Graph()
plot.Values(Filter(ast.shine)[1],x)
plot.Save("Gust")
plot=Graph()
plot.Values(Filter(ast.shine)[2],x)
plot.Save("Pad")"""

