print("enter name")
name1=input()
print("enter designation")
designation1=input()
print("enter salary")
salary1=int(input())
class employee:
    def __init__(self,name,designation,salary):
        self.name=name
        self.designation=designation
        self.salary=salary
    def f1(abc):
        print("name=",abc.name)
        print("designation=",abc.designation)
        print("salary=",abc.salary)
p1=employee(name1,designation1,salary1)
p1.f1()
