
from Geometry import *


linije=[]
step=pi/10
ref=Point(0,2)
refl=Line(ref,ref)

plot1=Graph()
plot=Graph()

lines=Circle(start=0,end=2*pi,increment=pi/2)
plot.Lines(lines,color="red")
plot1.Lines(Visible_Lines_From_Point(lines,ref))
plot.Save("filip")




