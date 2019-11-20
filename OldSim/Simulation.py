from Geometry import *

from math import pi,cos,sin
import numpy as np
import random


ast=Asteroid("Cardiotida")
as1=Asteroid()

x=Points(LoadTxt("cardiotida.txt"))
random.shuffle(x)

x1=Lines(x)

as1.Lines(x1)
as1.Plot()

x=FixPoints(x)

x2=Lines(x)

ast.Lines(x2)
ast.Plot()
Graph.Show()



#ast.Ellipse(increment=ast.increment,a=10,b=10)

#ast.Plot().Save(ast.name)

"""ast.Test(1)
ast.Save()"""

#ast.Test(1)


#plot.Save("Shine_"+ast.name+"_"+str(round(ast.increment,4))+"_"+str(ast.radius)+"_"+str(round(ast.phase,4)))

"""Graph.Show()"""
