print("enter radius")
r=int(input())
class circle:
    pi=3.14
    def __init__(self,r):
        self.r=r
    #def area1(abc):
       
    area=pi*r*r
    print("area of circle is:",area)
    cir=2*pi*r
    print("circumfrence of circle is:",cir)
obj1=circle(r)


