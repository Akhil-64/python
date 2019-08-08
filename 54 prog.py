print("enter size of list1")
a=int(input())
print("enter size of list2 less than list 1")
x=int(input())
list1=list()
list2=list()
list3=list()
list4=list()
print("enter list")
for i in range(0,a):
    b=input()
    list1.append(b)
print("list2")
for j in range(0,x):
    c=input()
    list2.append(c)
print(list1)
print(list2)
#print(list1[1]+list2[1]
if(a==x):
    for i in range(0,a):
       list3.append(list1[i]+list2[i])
    print(list3)
else:
     if(a>x):
         for i in range(0,a):
             list2.append("")
     print(list2)
     for i in range(0,a):
        list3.append(list1[i]+list2[i])
     print(list3)

