list1=[]
list2=[]
def f1(n):
    if(n%2==0) or (n%4==0):
        return n



for i in range(1,20):
    list1.append(i)
print(list1)
print(list(filter(f1,list1)))

print("enter size")
a=int(input())
list1=[]
print("enter list")
for i in range(0,a):
    list1.append(int(input()))
#print(list(filter(lambda x:x>0,list1)))
def my(n):
    if(n>0):
        return True
    else:
        return False
print(list(filter(my,list1)))

print("enter string")
a=input()
f1=map(lambda x:x.lower(),a)
l1=list(f1)
for i in l1:
    print(i,end="")

from functools import reduce
print("enter size")
a=int(input())
list1=[]
print("enter list")
for i in range(0,a):
    list1.append(int(input()))
print(reduce(lambda x,y:x if x>y else y,list1))

print("enter size")
a=int(input())
list1=[]
list2=[]
print("enter list")
for i in range(0,a):
         list1.append(input())
for i in list1:
    if(i==i[::-1]):
        list2.append("yes")
    else:
        list2.append("no")
print(list2)

from functools import reduce
l1=[22,33,22]
l2=[3,4,3,3]
l1.extend(l2)
print(l1)
def sum1(x1,y1):
    return x1+y1

print(reduce(sum1,l1))








