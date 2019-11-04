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
    
#print(name,list1)
#print(name2,list2)
#print(name3,list3)

class student:
    def __init__(self):
        self.n=0
        self.l=0
    def set(self,n,l):
        self.n=n
        self.l=l
    def __add__(self,other):
        return self.l+other.l

obj1=student()
obj1.set(name1,list1)
obj2=student()
obj1.set(name2,list2)
obj4=student()
obj4=obj1+obj2
print(obj4)
