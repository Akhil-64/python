print("enter size of list")
a=int(input())
list1=[]
print("enter list")
for i in range(0,a):
    x=input()
    list1.append(x)
print("original list")
print(list1)
list2=[]
list2=list1.copy()
print("copied list")
print(list2)
