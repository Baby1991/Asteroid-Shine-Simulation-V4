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

    def Sort_Points_By_Distance(self,points: list)->list:
        import operator
        
        points_with_dist=[]
        points1=[]

        for p in points:
            points_with_dist.append(
                (p.Distance(self),
                p)
                )

        for i in range(len(points_with_dist)):
            lowest_value_index = i
            for j in range(i + 1, len(points_with_dist)):
                if points_with_dist[j][0] < points_with_dist[lowest_value_index][0]:
                    lowest_value_index = j
            points_with_dist[i], points_with_dist[lowest_value_index] = points_with_dist[lowest_value_index], points_with_dist[i]

        for i in points_with_dist:
            points1.append(i[1])

        return points1

    def Sort_Lines_By_Distance(self,lines: list)->list:
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

    def Angle_Points(self,p1,p2)->float:
        #from math import atan2
        theta1 = atan3(p1.y-self.y,p1.x-self.x)
        theta2 = atan3(p2.y-self.y,p2.x-self.x)
        diff=abs(theta1-theta2)
        return(
            diff
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
    
    """def Angle_Lines(self,Line2,epsilon=0.001)->float:
        import math
        return(
            math.atan(
            abs(
                (Line2.k-self.k)
                /
                (1+(self.k*Line2.k))
                )
                )
                )"""
    
    """def Check_S_E_Match(self,epsilon=0.001)->bool:
        return self.start.Match(self.end,epsilon)"""

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

    """def Area_Lines(self,line)->float:
        A1=self.start.Area_Triangle(line.start,line.end)
        A2=self.start.Area_Triangle(self.end,line.end)
        return A1+A2"""
        
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

    """def And0(self,line,epsilon=0.001):

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
            return None"""

    def Continued(self,line,epsilon=0.001)->bool:
        
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
        return(
        (cos(incline)*cos(deflection))
        /
        (cos(incline)+cos(deflection))
        )
        #return 1

    def Line_Shine(self,observer,illuminator,Density:float=100,albedo=1)->float:
        points=self.Inerpolate(Density)
        #points=[self.Midpoint()]
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

    def Values(self,values:list,x:list=[],color="black",marker="."):
        import numpy
        from matplotlib.pyplot import plot
        if not x:
            x=numpy.arange(len(values))
        self.ax.plot(x,values,marker=marker,color=color)

    def Text(self,text:str="",x:float=0,y:float=0):
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

class Asteroid_Slice:
    
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

    def __init__(self,name="Asteroid",phase=pi/2,startPhase=0,increment=pi/2,radius=5,epsilon=0.001,Density:float=100):
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

    def Save(self,name:str="",path:str=""):
        
        if name is "":
            name=self.name
        SaveData(self,name,path)

    def Load(self,name:str="",path:str=""):
        
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

            """plot=Graph()        
            plot.Lines(lines1,linewidth=5)
            plot.Lines(visible,linewidth=3,color="blue")
            Graph.Show()"""

            for j in lines1:
                for l in visible:

                    if not j.Continued(l,epsilon):
                        temp=l.And(j,epsilon)

                        if temp:
                            
                            if temp.Return_Not_Zero(epsilon):
                                
                                """plot=Graph()
                                
                                plot.Lines(lines1,linewidth=5)
                                plot.Lines(output,linewidth=3,color="blue")
                                plot.Line(temp,linewidth=1,color="red")
                                Graph.Show()"""

                                if not any([p.Match(j,epsilon) for p in output]):
                                    output.append(j)

                        
        print(" "+self.name+"\tLines Fixed\tElapsed time:\t"+dhms(time.time()-fullstart))
        self.fixedLines=output
        return output

    def Test_Visibility(self,phase=pi/2,startPhase=0,increment=pi/2,radius=5,epsilon=0.001,force:bool=False)->list:
        import numpy
        from math import sin,cos
        import time

        """if not self.fixedLines or force:
            self.FixLines(epsilon,radius,increment)"""
        self.fixedLines=self.lines
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

            """plot=Graph()
            plot.Lines(self.fixedLines,linewidth=5)
            plot.Lines(visible,color="red")
            plot.Point(illuminator)
            plot.Point(observer)
            plot.Save(str(step))"""

            print_progress_bar(step,maxSteps,prefix=" "+self.name+"\tLine Visibility:\t",suffix="\t"+dhms(timeleft)+"\t",message=(" "+self.name+"\tVisibility Finished,\tElapsed Time = "+dhms(time.time()-start)))

        self.visible=output
        return output

    def Test_Shine(self,phase=pi/2,startPhase=0,increment=pi/2,radius=5,epsilon=0.001,Density:float=100,force:bool=False)->list:
        
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

    def Test(self,force:bool=0):
        import time
        import io
        from contextlib import redirect_stdout
        print("\tTesting:\t"+self.name)
        start=time.time()
        trap = io.StringIO()
        with redirect_stdout(trap):
            self.Test_Shine(self.phase,self.startPhase,self.increment,self.radius,self.epsilon,self.Density,force)
        
        elapsed=time.time()-start
        print("\t"+self.name+"\tElapsed time:\t"+dhms(elapsed))
        return self.shine

class Asteroid:
    
    trigs=[]
    shine=[]
    name=""
    path=""

    def __init__(self,name,path=""):
        import os
        with open(os.path.join(path,name)+".33") as txt:
            lines=txt.read().split('\n')
            trigs=[]
            for l in lines:
                l1=[]
                points=l.split('\t')
                for p in points:
                    coords=p.split(',')
                    p1=(float(coords[0]),float(coords[1]),float(coords[2]))
                    l1.append(p1)
                trigs.append(l1)

            self.trigs=trigs
            self.name=name
            self.path=path

    def Slice(self,Nmbr,epsilon=0.001):
        import numpy as np
        zs=[]
        for tr in self.trigs:
            zs.extend([tr[0][2],tr[1][2],tr[2][2]])
        zmax=max(zs)
        zmin=min(zs)
        step=(zmax-zmin)/(Nmbr+1)

        slices=[]
        for zeta in np.arange(zmin+step,zmax,step):
            sl=[]
            for tr in self.trigs:
                sl.extend(Trig_Plane_Intersect(tr,zeta,epsilon))
            if sl:
                slices.append(sl)

        self.slices=slices
        return slices

    def Test_Object(self,slices=100):
        import os,time
        print("Test for "+self.name+" starting")
        start=time.time()
        shine=[]
        self.Slice(slices)
        j=0
        for sl in self.slices:
            ast=Asteroid_Slice(name=self.name+"_"+str(j),phase=pi/9,increment=pi/36,radius=5000,Density=100)
            ast.Lines(sl)
            ast.Test()
            if not shine:
                shine=ast.shine
            else:
                for i in range(len(ast.shine)):
                    shine[i]=shine[i]+ast.shine[i]
            j+=1
        print("Testing for "+self.name+" ended. Elapsed Time: "+dhms(time.time()-start))
        self.shine=shine
        return shine

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

def Find_Visibly_Connected_Lines(lines:list,ref,epsilon=0.001)->tuple:
    for line in lines:
        for line1 in lines:
            if line is not line1:
                newline=ref.Visibly_Connected_Lines(line,line1,epsilon)
                if newline:
                    return((newline,line,line1))

def Find_Crossed_Lines(lines:list,epsilon=0.001)->tuple:
    for line in lines:
        for line1 in lines:
            if line is not line1:
                newlines=line.Divide(line1,epsilon)
                if newlines:
                    return((newlines,line,line1))

def Connect_Lines(lines:list,ref,epsilon=0.001)->list:
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

def Visible_Lines_From_Point(lines:list,ref,epsilon=0.001,connect=True):

    lines=ref.Sort_Lines_By_Distance(lines) #dobro
    sectors=[lines[0]] #dobro
    visible=[lines[0]] #dobro
    lines.pop(0) #dobro

    #max_ang,p1,p2=Max_Angular_Width(lines,ref) #proveriti
    #sectors.append(Line(p1,p2))
    #print(max_ang)
    #i=0
    for line in lines:

        """plot=Graph()
        plot.Lines(lines,linewidth=5)
        plot.Lines(sectors,linewidth=3,color="blue")
        plot.Lines(visible,linewidth=1,color="red")
        plot.Line(line,linewidth=1,color="green")
        plot.Save(str(i))"""

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

def And_Lines(lines1:list,lines2:list,epsilon=0.001):# ne radi / duple linije
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

def Visible_Line_From_Both_Points(lines:list,p1,p2,epsilon=0.001):
    visible1=Visible_Lines_From_Point(lines,p1,epsilon)
    visible2=Visible_Lines_From_Point(lines,p2,epsilon)
    return And_Lines(visible1,visible2,epsilon)

def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█',message=''):
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
        #shine+=round(line.Lenght())
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

def f(formula,**kwargs):
    import sympy
    expr=sympy.sympify(formula)
    return expr.evalf(subs=kwargs)

def dhms(seconds)->str:
    s=str(round(seconds%60,2))
    m=str(int((seconds//60)%60))
    h=str(int((seconds//3600)%24))
    d=str(int(seconds//(3600*24)))
    return(d+" d  "+h+" h  "+m+" min  "+s+" s")

def Sort(nums:list):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

def Find_Matching_Lines(lines:list,epsilon=0.001):
    for line in lines:
        for line1 in lines:
            if line is not line1:
                newlines=line.Match(line1,epsilon)
                if newlines:
                    return (line,line1)

def Remove_Matching_Lines(lines:list,epsilon=0.001):
    lines1=lines
    while Find_Matching_Lines(lines1,epsilon) is not None:
        _,line=Find_Matching_Lines(lines1,epsilon)
        lines1.remove(line)
    return lines1

def atan3(y:float,x:float,epsilon=0.001)->float:
    from math import atan,pi
    from numpy import sign
    if abs(x)<=epsilon:
        if abs(y)<=epsilon:
            return 0
        else:
            return sign(y)*pi/2
    else:
        return atan(y/x)

def Line_Plane_Intersect(i0,i1,zeta):
    x0,y0,z0=i0
    x1,y1,z1=i1
    t=(zeta-z0)/(z1-z0)
    A=x0+t*(x1-x0)
    B=y0+t*(y1-y0)
    return Point(A,B)

def Trig_Plane_Intersect(triangle,zeta,epsilon=0.001):
    points=list(triangle)
    points.sort(key=lambda x: x[2])
    #p,i = (x,y,z)
    p0=points[0]
    p1=points[1]
    p2=points[2]

    f0=abs(p0[2]-zeta)<=epsilon
    f1=abs(p1[2]-zeta)<=epsilon
    f2=abs(p2[2]-zeta)<=epsilon

    if p1[2]<zeta<p2[2]:
        r1=Line_Plane_Intersect(p1,p2,zeta)
        r2=Line_Plane_Intersect(p0,p2,zeta)
        return [Line(r1,r2)]

    elif p0[2]<zeta<p1[2]:
        r1=Line_Plane_Intersect(p0,p2,zeta)
        r2=Line_Plane_Intersect(p0,p1,zeta)
        return [Line(r1,r2)]

    elif f1 and p0[2]<zeta<p2[2]:
        r1=Point(p1[0],p1[1])
        r2=Line_Plane_Intersect(p0,p2,zeta)
        return [Line(r1,r2)]

    elif f2 and f1 and not f0:
        return [Line(Point(p2[0],p2[1]),Point(p1[0],p1[1]))]

    elif f0 and f1 and not f2:
        return [Line(Point(p0[0],p0[1]),Point(p1[0],p1[1]))]

    elif f0 and f1 and f2:
        
        return [
        Line(Point(p0[0],p0[1]),Point(p1[0],p1[1])),
        Line(Point(p0[0],p0[1]),Point(p2[0],p2[1])),
        Line(Point(p1[0],p1[1]),Point(p2[0],p2[1]))
        ]

    else:
        return []