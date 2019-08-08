print("enter list")
i=0
list1=list()
list2=[]
while(i!="@"):
    i=input()
    if(i=="@"):
       break
    else:
        list1.append(int(i))
print(list1)
list2=[]

for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)

