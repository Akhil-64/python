list1=[]
list2=[]
list3=[]

print("enter name1")
name1=input()
print("enter list1 of marks :")
for i in range(0,3):
    a=int(input())
    list1.append(a)

    
print("enter name2")
name2=input()
print("enter list2 of marks :")
for i in range(0,3):
    b=int(input())
    list2.append(b)

print("enter name3")
name3=input()
print("enter list3 of marks :")
for i in range(0,3):
    c=int(input())
    list3.append(c) 
class student:
    list4=[]
    def __init__(self,n):
        self.n=n
        self.l=[]
        
    def set(self,l):
        self.l=l

    def __add__(self,other):
        f=student(self.n)
        for i in range(0,3):
            f.l.append(self.l[i]+other.l[i])
        return f
    
    
    def display(self):
        print(self.n,self.l)
 
obj1=student(name1)
obj1.set(list1)
obj2=student(name2)
obj2.set(list2)
obj3=student(name3)
obj3.set(list3)
obj4=student(name1)
obj4=obj1+obj2+obj3
obj4.display()
