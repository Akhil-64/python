class myclass:
    x=5
print(myclass)
p1=myclass
print(p1.x)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p2=Person("john",36)
print(p2.name)
print(p2.age)

class Person2:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(abc):
        print("my name is",abc.name)
p3=Person2("john",102)
p3.myfunc()

class Person3:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(abc):
        print("my age is",abc.age)
p5=Person3("john",39)
p5.age=40
print(p5.age)

class Person4:
    def __init__(self,name,age):
        self.age=age
        self.name=name
    def myfunc(abc):
        print("my age is:",abc.age)
p6=Person4("john",83)
del p6.age
print(p6.name)
#print(p6.age)
del p6
print(p6)
