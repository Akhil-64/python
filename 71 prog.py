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
print("sorted on the base of name")
list2=sorted(list1,key=lambda x:x[0])
print(list2)
print("sorted on the base of age")
list3=sorted(list1,key=lambda x:x[1])
print(list3)
#print(list1,lambda x:x[1])
list4=[]
print("sorted on the base of height")
list4=sorted(list1,key=lambda x:x[2])
print(list4)
