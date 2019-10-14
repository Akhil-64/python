class student:
    list1=[]
    list2=[]
    list3=[]
    average=0
    sum1=0
    for i in range(0,2):
        print("roll number")
        __x=int(input())
        list1.append(__x)
        print("name")
        __y=input()
        list2.append(__y)
        print("marks")
        __z=int(input())
        list3.append(__z)
    print("details of student")
    print("roll numbers :")
    for j in list1:
        print(j)
    print("names :")
    for j in list2:
        print(j)
    print("marks :")
    for j in list3:
        print(j)
    sum1=sum(list3)
    def display(self):
        print("sum is :",self.sum1)
    def average_class(self):
        print("average is :",self.sum1/2)
    
        
obj1=student()
obj1.display()
obj1.average_class()


        
        
