from Geometry import *

from math import pi,cos,sin
import numpy as np

ast=Asteroid("Asteroid 1",increment=pi,phase=0)

ast.Ellipse(increment=pi/8,p=-1)
ast.Ellipse(increment=pi/8,p=1)
ast.Ellipse(increment=pi/8,q=-1)
ast.Ellipse(increment=pi/8 ,q=1)

#ast.Load("Asteroid 512 512 1024")

ast.Test()
ast.Save()
#Shutdown()

#ast.Plot().Save(ast.name)


"""for r in ast.visible[0][0]:
    print(r)
    """