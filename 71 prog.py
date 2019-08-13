print("enter size")
a=int(input())
tuple1=()
list1=[]
list2=[]
list3=[]
for i in range(0,a):
   print("enter name")
   name=str(input())
   print("enter age")
   age=int(input())
   print("enter height")
   height=int(input())
   tuple1=(name,age,height)
   list1.append(tuple1)
print("sorted on the base of name,height,age:")
list1.sort()
print(list1)


   



