print("enter element")
x=int(input())
list1=[]
list2=[]
list3=[]
print("enter list")
for i in range(0,x):
    a=input()
    list1.append(a)
print("n")
n=int(input())

for i in range(0,len(list1),n):
     list2.append(list1[i:i+n])
     
print(list2)
     
    

