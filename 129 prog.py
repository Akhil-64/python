class employee:
    print("enter first name")
    name=input()
    print("enter last name")
    last=input()
    print("enter age")
    age=int(input())
    print("enter designation")
    des=input()
class myclass(employee):
    print("name =",employee.name,"",employee.last)
    print("age =",employee.age)
    print("designation =",employee.des)
obj1=myclass()

    
