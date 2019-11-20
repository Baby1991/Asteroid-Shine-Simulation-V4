from Geometry import *

from math import pi,cos,sin
import numpy as np
import threading

ast=Asteroid("Cardiotida")
ast.Lines(LoadLines("cardiotida.txt"))

#ast.Ellipse(increment=ast.increment,a=10,b=10)

#ast.Plot().Save(ast.name)

"""ast.Test(1)
ast.Save()"""

#ast.Test(1)

t1=threading.Thread(target=ast.Thread, args=(0,pi/16,5))
t1.start()
t2=threading.Thread(target=ast.Thread, args=(0,pi/16,10))
t2.start()
t3=threading.Thread(target=ast.Thread, args=(0,pi/16,100))
t3.start()

t4=threading.Thread(target=ast.Thread, args=(0,pi/32,5))
t4.start()
t5=threading.Thread(target=ast.Thread, args=(0,pi/32,10))
t5.start()
t6=threading.Thread(target=ast.Thread, args=(0,pi/32,100))
t6.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t5.join()
print("Done")
#plot.Save("Shine_"+ast.name+"_"+str(round(ast.increment,4))+"_"+str(ast.radius)+"_"+str(round(ast.phase,4)))

"""Graph.Show()"""
