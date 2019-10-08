print("enter name")
n=input()
print("enter age")
a=int(input())
print("enter pay")
p=int(input())
class emp:
    def __init__(self,name,age,pay):
        self.name=name
        self.age=age
        self.pay=pay
    def myfunc1(abc):
        print("name is:",abc.name)
        print("age is:",abc.age)
    def myfunc2(d):
        d.pay2=(d.pay*0.1)+d.pay
        print("original pay is:",d.pay)
        print("incremented pay is:",d.pay2)
obj1=emp(n,a,p)
obj1.myfunc1()
obj1.myfunc2()
        
