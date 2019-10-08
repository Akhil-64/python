print("enter name")
n=input()
list1=[]
print("enter marks of 3 subjects")
for i in range(0,3):
    x=int(input())
    list1.append(x)
class student:
    list1=[]
    def __init__(self,name,l1):
        self.name=name
        self.l1=l1
    def myfunc(abc):
        #abc.list1.append(abc.l1)
        print("name =",abc.name)
        print("marks =",abc.l1)
obj1=student(n,list1)
obj1.myfunc()
    
