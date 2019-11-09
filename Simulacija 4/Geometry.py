#Geometry for Asteroid Shine Simulation

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

    def To_Tuple(self):
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
    
    def Check_S_E_Match(self,epsilon=0.001):
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
                
                angP1P2=observer.Angle_Points(occluder.start,occluder.end,epsilon)
                angOsLs=observer.Angle_Points(occluder.start,self.start,epsilon)
                angLsOe=observer.Angle_Points(self.start,occluder.end,epsilon)
                diff=angP1P2-(angOsLs+angLsOe)
                
                if abs(diff)<=epsilon:
                    return None
                else:
                    return self
            else:
                if pr1 is not None:

                    if y.Match(self.end,epsilon):
                        return None
                    else:
                        return [Line(y,self.end)]

                elif pr2 is not None:

                    if y.Match(self.start,epsilon):
                        return None
                    else:
                        return [Line(self.start,y)]

                else:
                    return None 
        else:
            if y is None:
                if pr1 is not None:

                    if z.Match(self.end,epsilon):
                        return None
                    else:
                        return [Line(z,self.end)]

                elif pr2 is not None:

                    if z.Match(self.start,epsilon):
                        return None
                    else:
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

                    if t1i.Check_S_E_Match(epsilon):

                        if t2i.Check_S_E_Match(epsilon):
                            return None
                        else:
                            return [t2i]

                    else:

                        if t2i.Check_S_E_Match(epsilon):
                            return [t1i]
                        else:
                            return [t1i,t2i]

                else:

                    if t1.Check_S_E_Match(epsilon):

                        if t2.Check_S_E_Match(epsilon):
                            return None
                        else:
                            return [t2]

                    else:

                        if t2.Check_S_E_Match(epsilon):
                            return [t1]
                        else:
                            return [t1,t2]
                    
    def vs_Sect(self,sectors,ref,epsilon=0.001)->list:
        return Lines_vs_Sectors([self],sectors,ref,epsilon)

class Graph:
    
    def __init__(self,x=7,y=7):
        from matplotlib.pyplot import figure
        self.fig=figure(figsize=(x,y))
        self.ax=self.fig.gca()

    def Point(self,p,color="black",marker="o"):
        from matplotlib.pyplot import plot
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

    def Save(self,name,path="",extenstion="png"):
        from matplotlib.pyplot import savefig
        import os
        saveFile=os.path.join(path,name)+"."+extenstion
        self.fig.savefig(saveFile)

    def Show():
        from matplotlib.pyplot import show
        show()


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

def Circle(p=0,q=0,r=1,start=0*pi,end=2*pi,increment=1/4*pi,SignificantDigits=6)->list:
    from math import pi,cos,sin
    import numpy
    lines=[]
    for i in numpy.arange(start,end,increment):
        t0=round(Point(r*cos(i)+p,r*sin(i)+q),SignificantDigits)
        t1=round(Point(r*cos(i+increment)+p,r*sin(i+increment)+q),SignificantDigits)
        l=Line(t0,t1)
        lines.append(l)
    return lines

def Lines_vs_Sect(lines:list,sector,ref,epsilon=0.001)->list:
    output=[]
    for line in lines:
        visible=line.Visibility(sector,ref,epsilon)
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
    lines=ref.Sort_Lines_By_Distance(lines)
    sectors=[lines[0]]
    visible=[lines[0]]
    lines.pop(0)
    for line in lines:
        temp=line.vs_Sect(sectors,ref,epsilon)
        if temp:
            sectors.extend(temp)
            visible.extend(temp)
            sectors=Connect_Lines(sectors,epsilon)
    return visible





"""
        def Intercept_Segment2(self,Line2,epsilon=0.001):
        k1=self.k
        k2=Line2.k
        n1=self.n
        n2=Line2.n
        if abs(k1-k2)>epsilon:
            x=(n2-n1)/(k1-k2)
            y=k1*x+n1
            p=Point(x,y)
            if( 
            self.On_Line(p)
            and
            Line2.On_Line(p)
            ):
                return p
            else:
                return None
        else:
            return None

    def Intercept_Segment_Line(self,Line1,epsilon=0.001):
        k1=self.k
        k2=Line1.k
        n1=self.n
        n2=Line1.n
        if abs(k1-k2)>epsilon:
            x=(n2-n1)/(k1-k2)
            y=k1*x+n1
            p=Point(x,y)
            if( 
            self.On_Line(p)
            ):
                return p
            else:
                return None
        else:
            return None
"""






    

    


    
        
        







    
