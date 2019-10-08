print("enter roll number")
roll=int(input())
print("enter name")
name=input()
print("enter marks")
marks=int(input())
class student:
    def __init__(self,roll,name,marks):
        self.roll=roll
        self.name=name
        self.marks=marks
    def myfunc(abc):
        print("roll number is",abc.roll)
        print("name is",abc.name)
        print("marks are",abc.marks)
p1=student(roll,name,marks)
p1.myfunc()
