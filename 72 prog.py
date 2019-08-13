print("enter paragarph")
a=str(input())
list1=a.split(" ")
list2=[]
count=0
for i in list1:
    count=list1.count(i)
    list2.append([i,count])
list4=[]
for i in list2:
    if i not in list4:
        list4.append(i)

for i in list4:
    #print(i)
    for j in i:
      print(j,end=" ")
    print()
    
