print("enter real1")
a=int(input())
print("enter img1")
b=int(input())
print("enter real2")
c=int(input())
print("enter img2")
d=int(input())

class complex1:
    def __init__(self):
        self.r=0
        self.i=0
    def set(self,r,i):
        self.i=i
        self.r=r
    def __add__(self,other):
        return self.r+other.r,self.i+other.i
    
c1=complex1()
c1.set(a,b)
c2=complex1()
c2.set(c,d)
c3=complex1()
c3=c1+c2
print(c3)
