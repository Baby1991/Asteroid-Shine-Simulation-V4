#Geometry for Asteroid Shine Simulation

from math import pi

class Point:    
    x=0
    y=0

    def __init__(self,x0,y0):
        self.x=x0
        self.y=y0
        self.value=(x0,y0)
    
    def __repr__(self):
        return repr(self.value) 
    
    def __call__(self):
        return self.value

    def __round__(self,SignificantDigits=0):
        return Point(round(self()[0],SignificantDigits),round(self()[1],SignificantDigits))

    def __sub__(self,p):
        return Point(self.x-p.x,self.y-p.y)

    def Match(self,p2,epsilon=0.001):
        import math
        d=math.sqrt(sum([(a - b) ** 2 for a, b in zip(self(), p2())]))
        if(d<=epsilon):
            return True
        else:
            return False

    def Sort_Lines_By_Distance(self,lines):
        import operator
        
        lines_with_dist=[]
        lines1=[]

        for line in lines:
            lines_with_dist.append(
                (line.Distance_To_Point(self),
                line)
                )

        for i in range(len(lines_with_dist)):
            lowest_value_index = i
            for j in range(i + 1, len(lines_with_dist)):
                if lines_with_dist[j][0] < lines_with_dist[lowest_value_index][0]:
                    lowest_value_index = j
                elif lines_with_dist[j][0] == lines_with_dist[lowest_value_index][0]:
                    l1=lines_with_dist[j][1]
                    l0=lines_with_dist[lowest_value_index][1]
                    a1=self.Angle_Points(l1.start,l1.end)
                    a0=self.Angle_Points(l0.start,l0.end)
                    if a1<a0: 
                        lowest_value_index = j
            lines_with_dist[i], lines_with_dist[lowest_value_index] = lines_with_dist[lowest_value_index], lines_with_dist[i]

        for i in lines_with_dist:
            lines1.append(i[1])

        return lines1

    def Angle_Points(self,p1,p2):
        #from math import atan2
        theta1 = atan3(p1.y-self.y,p1.x-self.x)
        theta2 = atan3(p2.y-self.y,p2.x-self.x)
        diff=abs(theta1-theta2)
        return(
            diff
            )

    def Distance(self,p):
        from math import sqrt
        return sqrt((self.x - p.x)**2 + (self.y - p.y)**2)

    def Closer_Point(self,p1,p2):
        if self.Distance(p1)<self.Distance(p2):
            return p1
        else:
            return p2
    
    def Area_Triangle(self,p1,p2):
        return abs(((p2.x*p1.y-p1.x*p2.y)-(p2.x*self.y-self.x*p2.y)+(p1.x*self.y-self.x*p1.y))/2)

    def Visibly_Connected_Lines(self,line1,line2,epsilon=0.001):
        p1=line1.start
        p2=line1.end
        p3=line2.start
        p4=line2.end

        if self.Area_Triangle(p1,p3)<=epsilon:
            return Line(p2,p4)
        elif self.Area_Triangle(p1,p4)<=epsilon:
            return Line(p2,p3)
        elif self.Area_Triangle(p2,p3)<=epsilon:
            return Line(p1,p4)
        elif self.Area_Triangle(p2,p4)<=epsilon:
            return Line(p1,p3)
        else:
            return None

class Line:
    start=Point(0,0)
    end=Point(0,0)
    k=0
    n=0

    def __init__(self,p1,p2):
        self.start=p1
        self.end=p2
        self.value=(p1,p2)
        self.k=self.Slope()
        self.n=self.yIntercept()
    
    def __repr__(self):
        return repr(self.value)
    
    def __call__(self):
        return self.value

    def __round__(self,SignificantDigits=0):
        p1=self.start
        p2=self.end
        p1=Point(round(p1()[0],SignificantDigits),round(p1()[1],SignificantDigits))
        p2=Point(round(p2()[0],SignificantDigits),round(p2()[1],SignificantDigits))
        return Line(p1,p2)

    def To_Tuple(self):
        x0=self.start.x
        y0=self.start.y
        x1=self.end.x
        y1=self.end.y
        return((x0,y0),(x1,y1))

    def Lenght(self):
        import math
        return(
                math.sqrt(
                    (self.end.x-self.start.x)**2
                    +
                    (self.end.y-self.start.y)**2
                )
            )

    def Midpoint(self):
        return(
            Point(
                (self.end.x+self.start.x)/2,
                (self.end.y+self.start.y)/2
                )
            )

    def On_Line(self,p,epsilon=0.001):
        return self.start.Distance(p)+self.end.Distance(p)-self.start.Distance(self.end)<=epsilon
    
    def Match(self,line,epsilon=0.001):
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

    def Angle_Of_Slope(self):
        import math
        p1,p2=self()
        x1,y1=p1()
        x2,y2=p2()
        return math.atan2((y2-y1),(x2-x1))

    def Slope(self):
        import math
        return(
            math.tan(self.Angle_Of_Slope())
            )

    def yIntercept(self):
        y=self.start.y
        x=self.start.x
        return(y-self.Slope()*x)

    def Intercept_Line2(self,Line1,epsilon=0.001):
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

    def Intercept_Segment2(self,Line2,epsilon=0.001):
        p=self.Intercept_Line2(Line2,epsilon)
        if p:
            if self.On_Line(p) and Line2.On_Line(p):
                return p
            else:
                return None
        else: 
            return None

    def Intercept_Segment_Line(self,Line2,epsilon=0.001):
        p=self.Intercept_Line2(Line2,epsilon)
        if p:
            if self.On_Line(p):
                return p
            else:
                return None
        else: 
            return None

    def Distance_To_Point(self,p,epsilon=0.001):
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

    def Visibility(self,occluder,observer,epsilon=0.001):
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
                    
    def vs_Sect(self,sectors,ref,epsilon=0.001):
        return Lines_vs_Sectors([self],sectors,ref,epsilon)
        
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

    def Continued(self,line,epsilon=0.001):
        
        if self.Match(line,epsilon):
            return False

        if self.start.Match(line.start,epsilon):
            start=self.end
            middle=self.start
            end=line.end
        elif self.start.Match(line.end,epsilon):
            start=self.end
            middle=self.start
            end=line.start
        elif self.end.Match(line.start,epsilon):
            start=self.start
            middle=self.end
            end=line.end
        elif self.end.Match(line.end,epsilon):
            start=self.start
            middle=self.end
            end=line.start
        else:
            return False

        a0,b0=start()
        a1,b1=middle()
        a2,b2=end()

        if abs(b2-b0)<=epsilon:
            a0,a1,a2,b0,b1,b2=b0,b1,b2,a0,a1,a2
            
        a=abs(a2-a1-(b2-b1)/(b2-b0)*(a2-a0))<=epsilon
        b=(b2-b0)>(b1-b0)
        
        return not a or b

    def Divide(self,line,epsilon=0.001):
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

    def Inerpolate(self,Density=100):
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

    def Closer_Angle(self,p1,ref):
        closer_Point=ref.Closer_Point(self.start,self.end)
        return abs(p1.Angle_Points(closer_Point,ref))

    def Point_Shine(self,p,observer,illuminator):
        from math import cos
        incline=min(self.Closer_Angle(p,illuminator),pi-self.Closer_Angle(p,illuminator))
        deflection=min(self.Closer_Angle(p,observer),pi-self.Closer_Angle(p,observer))
        return(
        (cos(incline)*cos(deflection))
        /
        (cos(incline)+cos(deflection))
        )

    def Line_Shine(self,observer,illuminator,Density=100,albedo=1):
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

    def Points(self,points,color="black",marker="o"):
        from matplotlib.pyplot import plot
        for p in points:
            self.ax.plot(p.x,p.y,marker=marker,color=color)

    def Line(self,line,color="black",linewidth=2,marker="."):
        from matplotlib.pyplot import plot
        xs=[line.start.x,line.end.x]
        ys=[line.start.y,line.end.y]
        self.ax.plot(xs,ys,linewidth=linewidth,marker=marker,color=color)

    def Lines(self,lines,color="black",linewidth=2,marker="."):
        from matplotlib.pyplot import plot
        for l in lines:
            xs=[l.start.x,l.end.x]
            ys=[l.start.y,l.end.y]
            self.ax.plot(xs,ys,linewidth=linewidth,marker=marker,color=color)

    def Values(self,values,x=[],color="black",marker="."):
        import numpy
        from matplotlib.pyplot import plot
        if not x:
            x=numpy.arange(len(values))
        self.ax.plot(x,values,marker=marker,color=color)

    def Text(self,text="",x=0,y=0):
        self.ax.text(x,y,text)

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
    
    lines=[]
    visible=[]
    shine=[]
    fixedLines=[]

    name=""
    phase=pi/2
    startPhase=0
    increment=pi/2
    radius=5
    epsilon=0.001
    Density=100

    def __init__(self,name="Asteroid",phase=pi/2,startPhase=0,increment=pi/2,radius=5,epsilon=0.001,Density=100):
        self.lines=[]
        self.visible=[]
        self.shine=[]
        self.fixedLines=[]

        self.name=name
        self.phase=phase
        self.startPhase=startPhase
        self.increment=increment
        self.radius=radius
        self.epsilon=epsilon
        self.Density=Density

    def __call__(self):
        return self.lines

    def __repr__(self):
        return repr(self.lines) 

    def Line(self,line):
        self.lines.append(line)

    def Lines(self,lines):
        for line in lines:
            self.lines.append(line)

    def Ellipse(self,p=0,q=0,a=1,b=1,start=0*pi,end=2*pi,increment=pi/4,SignificantDigits=6):
        from math import pi,cos,sin
        import numpy
        lines=[]
        for i in numpy.arange(start,end,increment):
            t0=round(Point(a*cos(i)+p,b*sin(i)+q),SignificantDigits)
            t1=round(Point(a*cos(i+increment)+p,b*sin(i+increment)+q),SignificantDigits)
            l=Line(t0,t1)
            lines.append(l)
        self.lines.extend(lines)

    def Function(self,xFunc,yFunc,p=0,q=0,a=1,b=1,start=0*pi,end=2*pi,increment=pi/4,SignificantDigits=6):
        from math import pi,cos,sin
        import numpy
        lines=[]
        for i in numpy.arange(start,end,increment):
            t0=round(Point(a*f(xFunc,t=i)+p,b*f(yFunc,t=i)+q),SignificantDigits)
            t1=round(Point(a*f(xFunc,t=i+increment)+p,b*f(yFunc,t=i+increment)+q),SignificantDigits)
            l=Line(t0,t1)
            lines.append(l)
        self.lines.extend(lines)

    def Plot(self):
        plot=Graph()
        plot.Lines(self.lines)
        return plot

    def Save(self,name="",path=""):
        
        if name is "":
            name=self.name
        SaveData(self,name,path)

    def Load(self,name="",path=""):
        
        if name is "":
            name=self.name
        Ast=LoadData(name,path)
        self.lines=Ast.lines
        self.visible=Ast.visible
        self.shine=Ast.shine
        self.fixedLines=Ast.fixedLines

        self.name=Ast.name
        self.phase=Ast.phase
        self.startPhase=Ast.startPhase
        self.increment=Ast.increment
        self.radius=Ast.radius
        self.epsilon=Ast.epsilon
        self.Density=Ast.Density

    def FixLines(self,epsilon=0.001,radius=5,increment=pi/2):
        import numpy
        from math import sin,cos,pi
        import time

        lines1=self.lines
        print(" "+self.name+"\tFixing Lines, This May Take A While...")
        fullstart=time.time()
        while Find_Crossed_Lines(lines1,epsilon): #NE RADI
            r=Find_Crossed_Lines(lines1,epsilon)
            lines1.remove(r[1])
            lines1.remove(r[2])
            lines1.extend(r[0])
        
        output=[]

        start=time.time()
        for t in numpy.arange(0,2*pi,increment):
            timeleft=Time_Left(start,time.time(),t,2*pi-increment)
            print_progress_bar(t,2*pi-increment,suffix="\t"+dhms(timeleft)+"\t")
            point=Point(radius*cos(t),radius*sin(t))
            visible=Visible_Lines_From_Point(lines1,point,epsilon,connect=True)

            for j in lines1:
                for l in visible:

                    if not j.Continued(l,epsilon):
                        temp=l.And(j,epsilon)

                        if temp:
                            
                            if temp.Return_Not_Zero(epsilon):

                                if not any([p.Match(j,epsilon) for p in output]):
                                    output.append(j)

                        
        print(" "+self.name+"\tLines Fixed\tElapsed time:\t"+dhms(time.time()-fullstart))
        self.fixedLines=output
        return output

    def Test_Visibility(self,phase=pi/2,startPhase=0,increment=pi/2,radius=5,epsilon=0.001,force=False):
        import numpy
        from math import sin,cos
        import time

        if not self.fixedLines or force:
            self.FixLines(epsilon,radius,increment)
        print("")
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
            timeleft=Time_Left(start,time.time(),step,maxSteps)

            print_progress_bar(step,maxSteps,prefix=" "+self.name+"\tLine Visibility:\t",suffix="\t"+dhms(timeleft)+"\t",message=(" "+self.name+"\tVisibility Finished,\tElapsed Time = "+dhms(time.time()-start)))

        self.visible=output
        return output

    def Test_Shine(self,phase=pi/2,startPhase=0,increment=pi/2,radius=5,epsilon=0.001,Density=100,force=False):
        
        if not self.visible or force:
            packets=self.Test_Visibility(phase,startPhase,increment,radius,epsilon,force)
            print("")
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

            timeleft=Time_Left(start,time.time(),step,maxSteps)
            
            print_progress_bar(step,maxSteps,prefix=" "+self.name+"\tLine Shine:\t\t",suffix="\t"+dhms(timeleft)+"\t",message=(" "+self.name+"\tShine Finished,\t\tElapsed Time = "+dhms(time.time()-start)))
        print("")
        self.shine=shines
        return shines

    def Test(self,force=0):
        import time
        start=time.time()
        self.Test_Shine(self.phase,self.startPhase,self.increment,self.radius,self.epsilon,self.Density,force)
        elapsed=time.time()-start
        print("Elapsed time:\t"+dhms(elapsed))
        return self.shine

    def Thread(self,phase,increment,radius):
        epsilon=0.001
        Density=100
        newself=self
        newself.Test_Shine(phase=phase,increment=increment,radius=radius,force=True,epsilon=epsilon,Density=Density)
        plot=Graph()
        plot.Values(newself.shine)
        plot.Save(self.name+"_"+str(round(increment,4))+"_"+str(radius)+"_"+str(round(phase,4)))

def Lines_Not_Matching(lines,epsilon=0.001):
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

def Find_Connected_Lines(lines,epsilon=0.001):
    for line in lines:
        for line1 in lines:
            if line is not line1:
                newline=line.Line_if_Touching(line1,epsilon)
                if newline:
                    return((newline,line,line1))

def Find_Visibly_Connected_Lines(lines,ref,epsilon=0.001):
    for line in lines:
        for line1 in lines:
            if line is not line1:
                newline=ref.Visibly_Connected_Lines(line,line1,epsilon)
                if newline:
                    return((newline,line,line1))

def Find_Crossed_Lines(lines,epsilon=0.001):
    for line in lines:
        for line1 in lines:
            if line is not line1:
                newlines=line.Divide(line1,epsilon)
                if newlines:
                    return((newlines,line,line1))

def Connect_Lines(lines,ref,epsilon=0.001):
    lines1=lines
    while Find_Connected_Lines(lines1,epsilon):
        r=Find_Connected_Lines(lines1,epsilon)
        lines1.remove(r[1])
        lines1.remove(r[2])
        lines1.append(r[0])
    while Find_Visibly_Connected_Lines(lines1,ref,epsilon):
        r=Find_Visibly_Connected_Lines(lines1,ref,epsilon)
        lines1.remove(r[1])
        lines1.remove(r[2])
        lines1.append(r[0])
    return lines1

def Lines_vs_Sect(lines,sector,ref,epsilon=0.001):
    output=[]
    for line in lines:
        visible=Lines_Not_Matching(line.Visibility(sector,ref,epsilon),epsilon)
        if visible is not None:
            output.extend(visible)
    if len(output)>0:
        return output
    else:
        return None

def Lines_vs_Sectors(lines,sectors,ref,epsilon=0.001):
    temp=lines
    for sect in sectors:
        temp=Lines_vs_Sect(temp,sect,ref,epsilon)
        if temp is None:    
            break
    return temp

def Visible_Lines_From_Point(lines,ref,epsilon=0.001,connect=True):

    lines=ref.Sort_Lines_By_Distance(lines) #dobro
    sectors=[lines[0]] #dobro
    visible=[lines[0]] #dobro
    lines.pop(0) #dobro

    #max_ang,p1,p2=Max_Angular_Width(lines,ref) #proveriti
    #sectors.append(Line(p1,p2))
    #print(max_ang)
    #i=0
    for line in lines:

        if connect:
            sectors=Connect_Lines(sectors,ref,epsilon)

        """if sectors[0].Match(Line(p1,p2),epsilon): #proveriti
            break"""

        #sectors=ref.Sort_Lines_By_Distance(sectors) #dobro

        temp=line.vs_Sect(sectors,ref,epsilon) #dobro   

        if temp is not None:
            sectors.extend(temp)
            visible.extend(temp)

        #i+=1

    return visible

def And_Lines(lines1,lines2,epsilon=0.001):# ne radi / duple linije
    #print(Find_Matching_Lines(lines1),Find_Matching_Lines(lines2)) 
    output=[]
    for line1 in lines1:
        for line2 in lines2:
            if line1.And(line2,epsilon):
                temp=line1.And(line2,epsilon).Return_Not_Zero(epsilon)
                if temp is not None:
                    output.append(temp)
    output=Remove_Matching_Lines(output,epsilon)
    #print(Find_Matching_Lines(output)) 
    return output

def Visible_Line_From_Both_Points(lines,p1,p2,epsilon=0.001):
    visible1=Visible_Lines_From_Point(lines,p1,epsilon)
    visible2=Visible_Lines_From_Point(lines,p2,epsilon)
    return And_Lines(visible1,visible2,epsilon)

def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='O',message=''):
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix)+'\r')
    if iteration == total:
        print('\n'+message)

def Time_Left(startTime,currentTime,step,maxSteps):
    passed=currentTime-startTime
    averageTime=passed/(step+1)
    return round(averageTime*(maxSteps-step),1)

def Lines_Shine(packet,Density=100):
    (lines,observer,illuminator)=packet
    shine=0
    for line in lines:
        shine+=line.Line_Shine(observer,illuminator,Density)
        #shine+=line.Lenght()
        #shine+=1
    return shine

def SaveData(data,name,path=""):
    import os,pickle
    saveFile=os.path.join(path,name)+".data"
    with open(saveFile,'wb') as filehandle:
        pickle.dump(data,filehandle)
    print("\tData written to:\t"+saveFile)

def LoadData(name,path=""):
    import os,pickle
    loadFile=os.path.join(path,name)+".data"
    with open(loadFile,'rb') as filehandle:
        data=pickle.load(filehandle)
    print("\tData loaded from:\t"+loadFile)
    return data

def LoadTxt(name,split="\n",path=""):
    with open(path+name) as file:
        return file.read().split(split)        

def LoadLines(name,split1="\n",split2=",",path=""):
    text=LoadTxt(name,split1,path)
    points=[]
    for txt in text:
        x,y=txt.split(',')
        points.append(Point(float(x),float(y)))
    lines=[]
    for i in range(-1,len(points)-1):
        lines.append(Line(points[i],points[i+1]))
    return lines

def Filter(data,cutoff=125):
    from scipy import signal
    import numpy
    data=numpy.array(data)
    b, a = signal.butter(8, cutoff/1000)
    y = signal.filtfilt(b, a, data, padlen=len(data)-1)

    return list(y)

def Shutdown():
    import os
    os.system('shutdown /p /f')

def f(formula,**kwargs):
    import sympy
    expr=sympy.sympify(formula)
    return expr.evalf(subs=kwargs)

def dhms(seconds):
    s=str(round(seconds%60,2))
    m=str(int((seconds//60)%60))
    h=str(int((seconds//3600)%24))
    d=str(int(seconds//(3600*24)))
    return(d+" d  "+h+" h  "+m+" min  "+s+" s")

def Sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

def Find_Matching_Lines(lines,epsilon=0.001):
    for line in lines:
        for line1 in lines:
            if line is not line1:
                newlines=line.Match(line1,epsilon)
                if newlines:
                    return (line,line1)

def Remove_Matching_Lines(lines,epsilon=0.001):
    lines1=lines
    while Find_Matching_Lines(lines1,epsilon) is not None:
        _,line=Find_Matching_Lines(lines1,epsilon)
        lines1.remove(line)
    return lines1

def atan3(y,x,epsilon=0.001):
    from math import atan,pi
    from numpy import sign
    if abs(x)<=epsilon:
        if abs(y)<=epsilon:
            return 0
        else:
            return sign(y)*pi/2
    else:
        return atan(y/x)