print("size")
n=int(input())
list1=[]
sum1=0
print("enter array")
for i in range(0,n):
    x=int(input())
    list1.append(x)
list2=[]
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if(list1[i]+list1[j]+list1[k]==0):
                print(list1[i],list1[j],list1[k])
                list2.append([list1[i],list1[j],list1[k]])
print(list2)
