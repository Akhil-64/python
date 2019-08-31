#remove duplicates
print("enter size of list")
a=int(input())
list1=[]
list2=[]
for i in range(0,a):
    x=int(input())
    list1.append(x)
#print(list1)
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)
