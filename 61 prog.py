print("enter list")
i=1
i2=0
list2=[]
list1=[]
while(i!=0):
    if(i==0):
        break
    else:
        i=int(input())
        list1.append(i)
        i2=i*10
        list2.append(i2)
print("original list:",list1)
print("original sorted list:",sorted(list1))
print("modified list",list2)
print("modified sorted list",sorted(list2))
