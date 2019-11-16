from ScannerTools import *

path="C:\\Users\\Filip\\Desktop\\Asteroidi\\Sfera"

shine=ScanImages(path)
shine = [x / 10000 for x in shine]
shine=Filter(shine)
plot=Graph()
plot.Values(shine)
plot.Save("ScannedShine")




