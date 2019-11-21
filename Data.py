from Geometry import Filter,Graph,LoadData
import os,sys

path=os.path.join(os.getcwd(),sys.argv[1])
name=sys.argv[2]

shine=LoadData(name,path)
plot=Graph()
plot.Values(shine)
plot.Save("shine",path)
plot=Graph()
plot.Values(Filter(shine))
plot.Save("filtered",path)