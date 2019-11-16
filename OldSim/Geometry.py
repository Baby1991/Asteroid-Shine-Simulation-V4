#Geometry for Asteroid Shine Simulation

from math import pi

class Point:
    x=0
    y=0

    def __init__(self,x0:float,y0:float):
        self.x=x0
        self.y=y0
        self.value=(x0,y0)
    
    def __repr__(self):
        return repr(self.value) 
    
    def __call__(self)->tuple:
        return self.value

    def __round__(self,SignificantDigits=0):
        return Point(round(self()[0],SignificantDigits),round(self()[1],SignificantDigits))

    def __sub__(self,p):
        return Point(self.x-p.x,self.y-p.y)

    def Match(self,p2,epsilon=0.001)->bool:
        import math
        d=math.sqrt(sum([(a - b) ** 2 for a, b in zip(self(), p2())]))
        if(d<=epsilon):
            return True
        else:
            return False

    def Sort_Lines_By_Distance(self,lines: list)->list:
        import operator
        
        lines_with_dist=[]
        lines1=[]

        for line in lines:
            lines_with_dist.append(
                (line.Distance_To_Point(self),
                line)
                )

        lines_with_dist.sort(key = operator.itemgetter(0))

        for i in lines_with_dist:
            lines1.append(i[1])

        return lines1

    def Angle_Points(self,p1,p2,epsilon=0.001)->float:
        from math import atan2
        return(
            atan2(p2.y-self.y,p2.x-self.x)
            -
            atan2(p1.y-self.y,p1.x-self.x)
            )

    def Distance(self,p)->float:
        from math import sqrt
        return sqrt((self.x - p.x)**2 + (self.y - p.y)**2)

    def Closer_Point(self,p1,p2):
        if self.Distance(p1)<self.Distance(p2):
            return p1
        else:
            return p2
    
    def Area_Triangle(self,p1,p2):
        return abs(((p2.x*p1.y-p1.x*p2.y)-(p2.x*self.y-self.x*p2.y)+(p1.x*self.y-self.x*p1.y))/2)

class Line:
    start=Point(0,0)
    end=Point(0,0)
    k=0
    n=0

    def __init__(self,p1:Point,p2:Point):
        self.start=p1
        self.end=p2
        self.value=(p1,p2)
        self.k=self.Slope()
        self.n=self.yIntercept()
    
    def __repr__(self):
        return repr(self.value)
    
    def __call__(self)->tuple:
        return self.value

    def __round__(self,SignificantDigits=0):
        p1=self.start
        p2=self.end
        p1=Point(round(p1()[0],SignificantDigits),round(p1()[1],SignificantDigits))
        p2=Point(round(p2()[0],SignificantDigits),round(p2()[1],SignificantDigits))
        return Line(p1,p2)

    def To_Tuple(self)->tuple:
        x0=self.start.x
        y0=self.start.y
        x1=self.end.x
        y1=self.end.y
        return((x0,y0),(x1,y1))

    def Lenght(self)->float:
        import math
        return(
                math.sqrt(
                    (self.end.x-self.start.x)**2
                    +
                    (self.end.y-self.start.y)**2
                )
            )

    def Midpoint(self)->Point:
        return(
            Point(
                (self.end.x+self.start.x)/2,
                (self.end.y+self.start.y)/2
                )
            )

    def On_Line(self,p:Point,epsilon=0.001)->bool:
        return self.start.Distance(p)+self.end.Distance(p)-self.start.Distance(self.end)<=epsilon
    
    def Match(self,line,epsilon=0.001)->bool:
        if (
            self.start.Match(line.start,epsilon) 
            and 
            self.end.Match(line.end,epsilon)
            ) or (
            self.start.Match(line.end,epsilon) 
            and 
            self.end.Match(line.start,epsilon)
            ):
            return True
        else:
            return False

    def Angle_Of_Slope(self)->float:
        import math
        p1,p2=self()
        x1,y1=p1()
        x2,y2=p2()
        return math.atan2((y2-y1),(x2-x1))

    def Slope(self)->float:
        import math
        return(
            math.tan(self.Angle_Of_Slope())
            )

    def yIntercept(self)->float:
        y=self.start.y
        x=self.start.x
        return(y-self.Slope()*x)
    
    def Angle_Lines(self,Line2,epsilon=0.001)->float:
        import math
        return(
            math.atan(
            abs(
                (Line2.k-self.k)
                /
                (1+(self.k*Line2.k))
                )
                )
                )
    
    def Check_S_E_Match(self,epsilon=0.001)->bool:
        return self.start.Match(self.end,epsilon)

    def Intercept_Line2(self,Line1,epsilon=0.001)->Point:
        line1=(self.start(),self.end())
        line2=(Line1.start(),Line1.end())

        xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
        ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]

        div = det(xdiff, ydiff)

        if abs(div) <= epsilon:
            return None
        else:
            d = (det(*line1), det(*line2))
            x = det(d, xdiff) / div
            y = det(d, ydiff) / div
            return Point(x, y)

    def Intercept_Segment2(self,Line2,epsilon=0.001)->Point:
        p=self.Intercept_Line2(Line2,epsilon)
        if p:
            if self.On_Line(p) and Line2.On_Line(p):
                return p
            else:
                return None
        else: 
            return None

    def Intercept_Segment_Line(self,Line2,epsilon=0.001)->Point:
        p=self.Intercept_Line2(Line2,epsilon)
        if p:
            if self.On_Line(p):
                return p
            else:
                return None
        else: 
            return None

    def Distance_To_Point(self,p,epsilon=0.001)->float:
        from numpy import arccos, array, dot, pi, cross
        from numpy.linalg import det, norm
        
        A=array([self.start.x,self.start.y])
        B=array([self.end.x,self.end.y])
        P=array([p.x,p.y])

        if all(abs(A-P)<=epsilon) or all(abs(B-P)<=epsilon):
            return 0
        if arccos(dot((P - A) / norm(P - A), (B - A) / norm(B - A))) > pi / 2:
            return norm(P - A)
        if arccos(dot((P - B) / norm(P - B), (A - B) / norm(A - B))) > pi / 2:
            return norm(P - B)
        return norm(cross(A-B, A-P))/norm(B-A)

    def Return_Not_Zero(self,epsilon=0.001):
        if self is not None:
            if self.start.Match(self.end,epsilon):
                return None
            else:
                return self
        else:
            return None

    def Line_if_Touching(self,other,epsilon=0.001):
        
        if(
            (
            self.start.Match(other.end,epsilon)
            and
            self.end.Match(other.start,epsilon)
            )
            or
            (
            self.start.Match(other.start,epsilon)
            and
            self.end.Match(other.end,epsilon)
            )
        ):

            return Line(self.start,self.end)
        
        elif(
            self.start.Match(other.start,epsilon)
        ):

            return Line(self.end,other.end)

        elif(
            self.start.Match(other.end,epsilon)
        ):

            return Line(self.end,other.start)

        elif(
            self.end.Match(other.start,epsilon)
        ):

            return Line(self.start,other.end)

        elif(
            self.end.Match(other.end,epsilon)
        ):

            return Line(self.start,other.start)

        else:
            return None

    def Visibility(self,occluder,observer,epsilon=0.001)->tuple:
        p1=Line(observer,occluder.start)
        p2=Line(observer,occluder.end)
        l1=Line(observer,self.start)
        l2=Line(observer,self.end)
        z=self.Intercept_Segment_Line(p1,epsilon)
        y=self.Intercept_Segment_Line(p2,epsilon)
        pr1=l1.Intercept_Segment2(occluder,epsilon)
        pr2=l2.Intercept_Segment2(occluder,epsilon)

        if z is None:
            if y is None:
                
                if pr1 is not None and pr2 is not None:
                    return None
                else:
                    return [self]

                """angP1P2=observer.Angle_Points(occluder.start,occluder.end,epsilon)   10.11.2019
                angOsLs=observer.Angle_Points(occluder.start,self.start,epsilon)
                angLsOe=observer.Angle_Points(self.start,occluder.end,epsilon)
                diff=angP1P2-(angOsLs+angLsOe)
                
                if abs(diff)<=epsilon:
                    return None
                else:
                    return self"""
            else:

                if pr1 is not None and pr2 is not None:
                    return None

                elif pr1 is not None:

                    return [Line(y,self.end)]

                elif pr2 is not None:

                    return [Line(self.start,y)]

                else:
                    return None 
        else:
            if y is None:

                if pr1 is not None and pr2 is not None:
                    return None

                elif pr1 is not None:

                    return [Line(z,self.end)]

                elif pr2 is not None:

                    return [Line(z,self.start)]

                else:
                    return None
            else:

                t1=Line(self.start,z)
                t2=Line(y,self.end)

                t1i=Line(self.start,y)
                t2i=Line(z,self.end)

                if(
                (
                t1.Lenght()
                +
                t2.Lenght()
                )
                >
                self.Lenght()-epsilon):

                    return [t1i,t2i]

                else:
                    return [t1,t2]
                    
    def vs_Sect(self,sectors,ref,epsilon=0.001)->list:
        return Lines_vs_Sectors([self],sectors,ref,epsilon)

    def Area_Lines(self,line)->float:
        A1=self.start.Area_Triangle(line.start,line.end)
        A2=self.start.Area_Triangle(self.end,line.end)
        return A1+A2
        
    def And(self,line,epsilon=0.001):   

        l1=self.On_Line(line.start,epsilon)
        l2=self.On_Line(line.end,epsilon)
        r1=line.On_Line(self.start,epsilon)
        r2=line.On_Line(self.end,epsilon)

        if r1:
            
            if r2:
                return self
            
            elif l2:
                return Line(self.start,line.end)

            else:
                return Line(self.start,line.start) 
        
        elif r2:

            if r1:
                return Line(self.end,line.start)
            
            else:
                return Line(self.end,line.end)
        
        elif l1:

            if l2:
                return line
            
            elif r2:
                return Line(line.start,self.end)
            
            else:
                return Line(line.start,self.start)

        elif l2:

            if r2:
                return Line(self.end,line.end)
            
            else:
                return Line(self.start,line.end)

        else:
            return None

    def And0(self,line,epsilon=0.001):

        l1=self.On_Line(line.start,epsilon)
        l2=self.On_Line(line.end,epsilon)
        r1=line.On_Line(self.start,epsilon)
        r2=line.On_Line(self.end,epsilon)

        if l1 and l2 and r1 and r2:
            return Line(self.start,self.end)

        if l1 and l2 and not r1 and not r2:
            return Line(self.start,self.end)

        elif not l1 and not l2 and r1 and r2: 
            return Line(line.start,line.end)

        else:
            return None

    def Continued(self,line,epsilon=0.001)->bool:
        l1=self.start.Match(line.start,epsilon)
        l2=self.start.Match(line.end,epsilon)
        l3=self.end.Match(line.start,epsilon)
        l4=self.end.Match(line.end,epsilon)
        l=[l1,l2,l3,l4]

        r1=self.On_Line(line.start,epsilon)
        r2=self.On_Line(line.end,epsilon)
        r3=line.On_Line(self.start,epsilon)
        r4=line.On_Line(self.end,epsilon)
        r=[r1,r2,r3,r4]

        return NmbrTrue(l,1) and NmbrTrue(r,2)

    def Divide(self,line,epsilon=0.001)->list:
        if not self.Continued(line,epsilon):
            cross=self.Intercept_Segment2(line,epsilon)
            if cross is not None:
                output=[]
                l1=Line(self.start,cross)
                l2=Line(self.end,cross)
                l3=Line(line.start,cross)
                l4=Line(line.end,cross)

                if l1.Return_Not_Zero(epsilon) is not None:
                    output.append(l1)
                if l2.Return_Not_Zero(epsilon) is not None:
                    output.append(l2)
                if l3.Return_Not_Zero(epsilon) is not None:
                    output.append(l3)
                if l4.Return_Not_Zero(epsilon) is not None:
                    output.append(l4)

                if len(output):
                    return output
                else:
                    return None

        else:
            return None    

    def Inerpolate(self,Density:float=100)->list:
        import numpy
        number_of_points=max(int(Density*self.Lenght()),1)
        
        x0=self.start.x
        y0=self.start.y
        x1=self.end.x
        y1=self.end.y
        k=self.k
        n=self.n
        dx=abs(x1-x0)
        dy=abs(y1-y0)
        xstep=dx/number_of_points
        ystep=dy/number_of_points
        output=[]
        
        if ystep>xstep:
            for y in numpy.arange(min(y0,y1),max(y0,y1)+ystep,ystep):
                output.append(Point((y-n)/k,y))
        else:
            for x in numpy.arange(min(x0,x1),max(x0,x1)+xstep,xstep):
                output.append(Point(x,k*x+n))

        return output

    def Closer_Angle(self,p1,ref)->float:
        closer_Point=ref.Closer_Point(self.start,self.end)
        return abs(p1.Angle_Points(closer_Point,ref))

    def Point_Shine(self,p,observer,illuminator)->float:
        from math import cos
        incline=min(self.Closer_Angle(p,illuminator),pi-self.Closer_Angle(p,illuminator))
        deflection=min(self.Closer_Angle(p,observer),pi-self.Closer_Angle(p,observer))
        """"return(
        (cos(incline)*cos(deflection))
        /
        (cos(incline)+cos(deflection))
        )
        """
        return 1

    def Line_Shine(self,observer,illuminator,Density:float=100,albedo=1)->float:
        points=self.Inerpolate(Density)
        shine=0
        for p in points:
            shine+=(albedo*self.Point_Shine(p,observer,illuminator))
        shine=shine*self.Lenght()/len(points)
        return shine

class Graph:
    
    def __init__(self,x=7,y=7):
        from matplotlib.pyplot import figure
        self.fig=figure(figsize=(x,y))
        self.ax=self.fig.gca()

    def Point(self,p,color="black",marker="o"):
        from matplotlib.pyplot import plot
        self.ax.plot(p.x,p.y,marker=marker,color=color)

    def Points(self,points:list,color="black",marker="o"):
        from matplotlib.pyplot import plot
        for p in points:
            self.ax.plot(p.x,p.y,marker=marker,color=color)

    def Line(self,line,color="black",linewidth=2,marker="."):
        from matplotlib.pyplot import plot
        xs=[line.start.x,line.end.x]
        ys=[line.start.y,line.end.y]
        self.ax.plot(xs,ys,linewidth=linewidth,marker=marker,color=color)

    def Lines(self,lines:list,color="black",linewidth=2,marker="."):
        from matplotlib.pyplot import plot
        for l in lines:
            xs=[l.start.x,l.end.x]
            ys=[l.start.y,l.end.y]
            self.ax.plot(xs,ys,linewidth=linewidth,marker=marker,color=color)

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

class Asteroid:
    name=""
    lines=[]
    visible=[]
    shine=[]
    fixedLines=[]

    def __init__(self,name="Asteroid"):
        self.lines=[]
        self.visible=[]
        self.shine=[]
        self.fixedLines=[]
        self.name=name

    def __call__(self,epsilon=0.001):
        lines1=self.lines
        i=0
        print('\r %s\tFixing Lines:\t%s' % (self.name,i*"*"+(5-i)*"."), end='\r')
        while Find_Crossed_Lines(lines1,epsilon):
            print('\r %s\tFixing Lines:\t%s' % (self.name,i*"*"+(5-i)*"."), end='\r')
            r=Find_Crossed_Lines(lines1,epsilon)
            lines1.remove(r[1])
            lines1.remove(r[2])
            lines1.extend(r[0])
            i=(i+1)%6
        print(print(' %s\tLines Fixed!\n' % (self.name)))
        return lines1

    def __repr__(self):
        return repr(self.lines) 

    def Line(self,line):
        self.lines.append(line)

    def Circle(self,p=0,q=0,r=1,start=0*pi,end=2*pi,increment=1/4*pi,SignificantDigits=6):
        from math import pi,cos,sin
        import numpy
        lines=[]
        for i in numpy.arange(start,end,increment):
            t0=round(Point(r*cos(i)+p,r*sin(i)+q),SignificantDigits)
            t1=round(Point(r*cos(i+increment)+p,r*sin(i+increment)+q),SignificantDigits)
            l=Line(t0,t1)
            lines.append(l)
        self.lines.extend(lines)

    def Plot(self):
        plot=Graph()
        plot.Lines(self.lines)
        return plot

    def Save(self,name:str="",path:str="",lines:str="",visible:str="",shine:str="",fixedLines:str=""):
        
        if name is "":
            name=self.name
        SaveData(self,name,path)

        if self.lines and lines:
            SaveData(self.lines,lines,path)

        if self.visible and visible:
            SaveData(self.visible,visible,path)

        if self.shine and shine:
            SaveData(self.shine,shine,path)

        if self.fixedLines and fixedLines:
            SaveData(self.fixedLines,fixedLines,path)

    def Load(self,name:str="",lines:str="",fixedLines:str="",visible:str="",shine:str="",path:str=""):
        
        if name is not "":
            self.lines=LoadData(name,path).lines
            self.visible=LoadData(name,path).visible
            self.shine=LoadData(name,path).shine
            self.fixedLines=LoadData(name,path).fixedLines

        if lines is not "":
            self.lines=LoadData(lines,path)

        if visible is not "":
            self.visible=LoadData(visible,path)

        if shine is not "":
            self.shine=LoadData(shine,path)

        if fixedLines is not "":
            self.fixedLines=LoadData(fixedLines,path)

    def Test_Visibility(self,phase=pi/2,startPhase=0,increment=pi/2,radius=5,epsilon=0.001,save:bool=False)->list:
        import numpy
        from math import sin,cos
        import time

        if not self.fixedLines:
            self.fixedLines=self()

        print_progress_bar(0,1,prefix=" "+self.name+"\tLine Visibility:\t")
        
        output=[]
        start=time.time()
        
        maxSteps=(2*pi/increment)-1

        for t in numpy.arange(startPhase,2*pi+startPhase,increment):
            
            observer=Point(radius*cos(t),radius*sin(t))
            illuminator=Point(radius*cos(t+phase),radius*sin(t+phase))
            
            visible=Visible_Line_From_Both_Points(self.fixedLines,observer,illuminator,epsilon)

            output.append((visible,illuminator,observer))

            step=t/increment

            print_progress_bar(step,maxSteps,prefix=" "+self.name+"\tLine Visibility:\t",suffix="\t"+str(Time_Left(start,time.time(),step,maxSteps)),message=(" "+self.name+"\tVisibility Finished,\tElapsed Time = "+str(round(time.time()-start,1))))
        
        if save:
            SaveData(output,self.name+"_visibility")

        self.visible=output
        return output
    
    def Test_Shine(self,phase=pi/2,startPhase=0,increment=pi/2,radius=5,epsilon=0.001,Density:float=100,save:bool=False)->list:
        
        if not self.visible:
            packets=self.Test_Visibility(phase,startPhase,increment,radius,epsilon)
        else:
            packets=self.visible
        
        import time
        shines=[]
        start=time.time()
        maxSteps=len(packets)-1
        print_progress_bar(0,1,prefix=" "+self.name+"\tLine Shine:\t\t")
        for l in packets:
            shines.append(Lines_Shine(l,Density))
            step=packets.index(l)
            print_progress_bar(step,maxSteps,prefix=" "+self.name+"\tLine Shine:\t\t",suffix="\t"+str(Time_Left(start,time.time(),step,maxSteps)),message=(" "+self.name+"\tShine Finished,\t\tElapsed Time = "+str(round(time.time()-start,1))))
        
        if save:
            SaveData(shines,self.name+"_shine")

        self.shine=shines
        return shines

def Lines_Not_Matching(lines:list,epsilon=0.001)->list:
    output=[]
    if lines is not None:
        for line in lines:
            if line.Return_Not_Zero(epsilon) is not None:
                output.append(line)

        if len(output)>0:
            return output
        else:
            return None
    else:
        return None

def Find_Connected_Lines(lines:list,epsilon=0.001)->tuple:
    for line in lines:
        for line1 in lines:
            if line is not line1:
                newline=line.Line_if_Touching(line1,epsilon)
                if newline:
                    return((newline,line,line1))

def Connect_Lines(lines:list,epsilon=0.001)->list:
    lines1=lines
    while Find_Connected_Lines(lines1,epsilon):
        r=Find_Connected_Lines(lines1,epsilon)
        lines1.remove(r[1])
        lines1.remove(r[2])
        lines1.append(r[0])
    return lines1

def Lines_vs_Sect(lines:list,sector,ref,epsilon=0.001)->list:
    output=[]
    for line in lines:
        visible=Lines_Not_Matching(line.Visibility(sector,ref,epsilon),epsilon)
        if visible is not None:
            output.extend(visible)
    if len(output)>0:
        return output
    else:
        return None

def Lines_vs_Sectors(lines:list,sectors:list,ref,epsilon=0.001)->list:
    temp=lines
    for sect in sectors:
        temp=Lines_vs_Sect(temp,sect,ref,epsilon)
        if temp is None:    
            break
    return temp

def Visible_Lines_From_Point(lines:list,ref,epsilon=0.001):
    
    lines=ref.Sort_Lines_By_Distance(lines) #dobro
    sectors=[lines[0]] #dobro
    visible=[lines[0]] #dobro
    lines.pop(0) #dobro

    for line in lines:

        sectors=Connect_Lines(sectors,epsilon)

        sectors=ref.Sort_Lines_By_Distance(sectors) #dobro

        temp=line.vs_Sect(sectors,ref,epsilon) #dobro

        if temp is not None:
            sectors.extend(temp)
            visible.extend(temp)

    return visible

def And_Lines(lines1:list,lines2:list,epsilon=0.001):
    output=[]
    for line1 in lines1:
        for line2 in lines2:
            if line1.And(line2,epsilon):
                temp=line1.And(line2,epsilon).Return_Not_Zero(epsilon)
                if temp is not None:
                    output.append(temp)
    
    #print(len(lines1),len(lines2),len(output),len(output1))        
    return output

def Visible_Line_From_Both_Points(lines:list,p1,p2,epsilon=0.001):
    visible1=Visible_Lines_From_Point(lines,p1,epsilon)
    visible2=Visible_Lines_From_Point(lines,p2,epsilon)
    return And_Lines(visible1,visible2,epsilon)

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

def Lines_Shine(packet:tuple,Density:float=100):
    (lines,observer,illuminator)=packet
    shine=0
    for line in lines:
        shine+=line.Line_Shine(observer,illuminator,Density)
        #shine+=line.Lenght()
        #shine+=1
    return shine

def SaveData(data:list,name:str,path:str=""):
    import os,pickle
    saveFile=os.path.join(path,name)+".data"
    with open(saveFile,'wb') as filehandle:
        pickle.dump(data,filehandle)
    print("\tData written to:\t"+saveFile)

def LoadData(name:str,path:str="")->list:
    import os,pickle
    loadFile=os.path.join(path,name)+".data"
    with open(loadFile,'rb') as filehandle:
        data=pickle.load(filehandle)
    print("\tData loaded from:\t"+loadFile)
    return data

def NmbrTrue(bools:list,num:int)->bool:
    i=0
    for t in bools:
        if t:
            i+=1
    if i==num:
        return True
    else:
        return False
    
def Find_Crossed_Lines(lines:list,epsilon=0.001)->tuple:
    for line in lines:
        for line1 in lines:
            if line is not line1:
                newlines=line.Divide(line1,epsilon)
                if newlines:
                    return((newlines,line,line1))

def Filter(data:list,cutoff:float=125)->list:
    from scipy import signal
    import numpy
    data=numpy.array(data)
    b, a = signal.butter(8, cutoff/1000)
    y = signal.filtfilt(b, a, data, padlen=len(data)-1)
    return list(y)

def Shutdown():
    import os
    os.system('shutdown /p /f')

"""def Valid_Lines(lines:list,epsilon=0.001)->list:
    lines1=lines
    while Find_Crossed_Lines(lines1,epsilon):
        r=Find_Crossed_Lines(lines1,epsilon)
        lines1.remove(r[1])
        lines1.remove(r[2])
        lines1.extend(r[0])
    return lines1"""

"""def Test_Lines(lines:list,phase=pi/2,startPhase=0,increment=pi/2,radius=5,epsilon=0.001):
    import numpy
    from math import sin,cos
    import time

    print_progress_bar(0,1,prefix="\tLine Visibility:\t")
    
    output=[]
    start=time.time()
    
    maxSteps=(2*pi/increment)-1

    for t in numpy.arange(startPhase,2*pi+startPhase,increment):
        
        observer=Point(radius*cos(t),radius*sin(t))
        illuminator=Point(radius*cos(t+phase),radius*sin(t+phase))
        
        visible=Visible_Line_From_Both_Points(lines,observer,illuminator,epsilon)

        output.append((visible,illuminator,observer))

        step=t/increment

        print_progress_bar(step,maxSteps,prefix="\tLine Visibility:\t",suffix="\t"+str(Time_Left(start,time.time(),step,maxSteps)),message=("\tVisibility Finished,\tElapsed Time = "+str(round(time.time()-start,1))))
    
    return output"""

"""def Shine(packets:list,Density:float=100):
    import time
    shines=[]
    start=time.time()
    maxSteps=len(packets)-1
    print_progress_bar(0,1,prefix="\tLine Shine:\t\t")
    for l in packets:
        shines.append(Lines_Shine(l,Density))
        step=packets.index(l)
        print_progress_bar(step,maxSteps,prefix="\tLine Shine:\t\t",suffix="\t"+str(Time_Left(start,time.time(),step,maxSteps)),message=("\tShine Finished,\t\tElapsed Time = "+str(round(time.time()-start,1))))
    return shines"""

"""def Circle(p=0,q=0,r=1,start=0*pi,end=2*pi,increment=1/4*pi,SignificantDigits=6)->list:
    from math import pi,cos,sin
    import numpy
    lines=[]
    for i in numpy.arange(start,end,increment):
        t0=round(Point(r*cos(i)+p,r*sin(i)+q),SignificantDigits)
        t1=round(Point(r*cos(i+increment)+p,r*sin(i+increment)+q),SignificantDigits)
        l=Line(t0,t1)
        lines.append(l)
    return lines"""