import math
print("add num")
num=int(input())
print("add den")
den=int(input())
print("add num1")
num1=int(input())
print("add den1")
den1=int(input())
class fraction:
    def __init__(self):
        self.n=0
        self.d=0
    def set(self,n,d):
        self.n=n
        self.d=d
    def __add__(self,other):
        f=fraction()
        n=(self.n*other.d)+(other.n*self.d)
        d=self.d*other.d
        a=math.gcd(n,d)
        f.n=n/a
        f.d=d/a
        #print("num",n)
        #print("den",d)
        #print("gcd",a)
        #print(f.n)
        #print(f.d)
        #f.a=math.gcd(den,den1)
        return f


    def display(self):
        print(self.n,"/",self.d)
        
obj1=fraction()
obj1.set(num,den)
obj2=fraction()
obj2.set(num1,den1)
obj3=fraction()
obj3=obj1+obj2
obj3.display()



        
