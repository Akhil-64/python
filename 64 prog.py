print("enter size")
a=int(input())
list1=[]
print("enter list")
for i in range(0,a):
    x=input()
    list1.append(x)
print("enter n")
n=int(input())
count=0
list2=[]
c=0
for i in range(0,n):
    count+=1
    for i in range(0,a):
        list2.append(list1[i]+str(count))
        #print(list1[i],count)
print(list2)
    
    

