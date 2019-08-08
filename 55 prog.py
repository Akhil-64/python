print("enter size")
a=int(input())
list1=list()
list2=list()
list3=list()
for i in range(0,a):
    x=input()
    list1.append(x)
for i in range(0,a):
    list2.append(list1[i][0])
print(list2)

list4=[]
for i in list2:
    if i not in list4:
        x=i.lower()
        list4.append(x)
print("list4 is:",list4)
list5=[]
for i in list4:
    if i not in list5:
        list5.append(i)
print("list5 is:",list5)
    

    
