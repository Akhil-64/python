print("enter size of list")
a=int(input())
list1=[]
for i in range(0,a):
    x=input()
    list1.append(x)
print(list1)
d1=dict()
d2=dict()
for i in list1[::-1]:
    d1[i]=d2
    d2=d1
    d1={}
print(d2)
