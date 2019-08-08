print("enter n")
n=int(input())
print("enter m")
m=int(input())
print("skip")
skip=int(input())
list1=list()
list2=list()
for i in range(n,m):
    list1.append(i)
print(list1)
cd=list1.index(m-1)
print(cd)
list2=list1[0:cd:skip]
print(list2)

    
