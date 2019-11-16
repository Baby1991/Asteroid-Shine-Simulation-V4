class Graph:
    
    def __init__(self,x=7,y=7):
        from matplotlib.pyplot import figure
        self.fig=figure(figsize=(x,y))
        self.ax=self.fig.gca()

    def Values(self,values:list,color="black",marker="."):
        import numpy
        from matplotlib.pyplot import plot
        x=numpy.arange(len(values))
        self.ax.plot(x,values,marker=marker,color=color)

    def Save(self,name,path="",extenstion="png"):
        from matplotlib.pyplot import savefig
        import os
        saveFile=os.path.join(path,name)+"."+extenstion
        self.fig.savefig(saveFile)
        print("\tImage Saved:\t\t"+saveFile)

    def Show():
        from matplotlib.pyplot import show
        show()

def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█',message=''):
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end='\r')
    if iteration == total:
        print('\n'+message)

def Time_Left(startTime:float,currentTime:float,step:int,maxSteps:int):
    passed=currentTime-startTime
    averageTime=passed/(step+1)
    return round(averageTime*(maxSteps-step),1)

def ScanImage(src):
    import time,cv2,os
    import numpy as np
    ret, img = cv2.threshold(src, 2, 255, cv2.THRESH_BINARY) 

    #img=cv2.erode(img,np.ones((3,3)),iterations=20)
    #img=cv2.dilate(img,np.ones((3,3)),iterations=20)
    new_image = src * ((img/255).astype(src.dtype))
    return(sum(sum(new_image)))

def ScanImages(path:str=""):
    import time,cv2,os
    imageList=os.listdir(path)
    maxSteps=len(imageList)-1
    shine=[]
    step=0
    print_progress_bar(0,1,prefix="\tCompiling Scan:\t")
    start=time.time()
    for i in imageList:
        print_progress_bar(step,maxSteps,prefix="\tCompiling Scan:\t",suffix=str(Time_Left(start,time.time(),step,maxSteps)))
        src =cv2.imread(os.path.join(path,i),cv2.IMREAD_GRAYSCALE)
        shine.append(ScanImage(src))
        step+=1
    return shine

def Filter(data:list,cutoff:float=125)->list:
    from scipy import signal
    import numpy
    data=numpy.array(data)
    b, a = signal.butter(8, cutoff/1000)
    y = signal.filtfilt(b, a, data, padlen=len(data)-1)
    return list(y)