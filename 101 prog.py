print("enter size")
a=int(input())
print("enter list")
list1=[]
for i in range(0,a):
    x=int(input())
    list1.append(x)
print(list1)
print(list(filter(lambda x:x>0,list1)))
