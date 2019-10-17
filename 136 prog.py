import math
print("enter radius")
r=float(input())
print("enter height")
h=float(input())
class shade:
    def __init__(self,r,h):
        self.r=r
        self.h=h
        
    def display1(self):
        area1=3.14*self.r*self.r
        print("area of circle:",area1)
        
    def display2(self):
        a=3.14*self.r
        b=self.r+(math.sqrt(h**2+r**2))
        print("area of cone:",a*b)
        
class circle(shade):
    def __init__(self,r,h):
        #super().__init__(r,h)
        shade.__init__(self,r,h)
   #def display(self):
        #print("area of circle:",3.14*self.r*self.r)
class cone(shade):
    def __init__(self,r,h):
        shade.__init__(self,r,h)

    
obj1=circle(r,h)
obj1.display1()
obj2=cone(r,h)
obj2.display2()
