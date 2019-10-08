print("enter firstname")
x=input()
print("enter lastname")
y=input()
class student:
    def __init__(self,first,last):
        self.first=first
        self.last=last
    def myfunc(abc):
        print(abc.first,".",abc.last,"@chitkara.edu.in")
obj1=student(x,y)
obj1.myfunc()

