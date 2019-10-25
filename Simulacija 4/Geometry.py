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
    
    def Match(self,p2,epsilon=0.001)->bool:
        import math
        d=math.sqrt(sum([(a - b) ** 2 for a, b in zip(self(), p2())]))
        if(d<=epsilon):
            return True
        else:
            return False

    def Sort_Lines_By_Distance(self,lines: list, SignificantDigits=10)->list:
        import operator
        
        lines_with_dist=[]
        lines1=[]

        for line in lines:
            lines_with_dist.append(
                (round(line.Distance_To_Point(self),SignificantDigits),
                line)
                )

        lines_with_dist.sort(key = operator.itemgetter(0))

        for i in lines_with_dist:
            lines1.append(i[1])

        return lines1

    #def Visible_Lines_From_A_Point(self, sorted_Lines:list)->list:


        

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
        return(Point((self.end.x+self.start.x)/2,(self.end.y+self.start.y)/2))
    
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
    
    def Angle(self,Line2,epsilon=0.001)->float:
        import math
        if( 
        (self.k-Line2.k)<=epsilon 
        and 
        (self.n-Line2.n)<=epsilon
        ):
            return None
        else:
            return(
                math.atan(
                abs(
                    (Line2.k-self.k)
                    /
                    (1+(self.k*Line2.k))
                )
                )
                )

    def Intercept(self,Line2,epsilon=0.001,SignificantDigits=6):
        k1=self.k
        k2=Line2.k
        n1=self.n
        n2=Line2.n
        if k1 != k2:
            x=(n2-n1)/(k1-k2)
            y=k1*x+n1
            if( 
            (self.start.x-epsilon<=x)
            and
            (self.end.x+epsilon>=x)
            and
            (Line2.start.x-epsilon<=x)
            and
            (Line2.end.x+epsilon>=x)
            ):
                return Point(
                round(x,SignificantDigits),
                round(y,SignificantDigits)
                )
            else:
                return None
        else:
            return None

    def Distance_To_Point(self,p)->float:
        return(Line(self.Midpoint(),p).Lenght())

    def Line_start1_end2_if_Touching(self,other,epsilon=0.001):
        if self.end.Match(other.start,epsilon):
            return(Line(self.start,other.end))
        elif self.start.Match(other.end,epsilon):
            return(Line(other.start,self.end))
        else:
            return None

def Connect_Lines(lines:list,epsilon=0.001)->list:


    

    


    
        
        







    
