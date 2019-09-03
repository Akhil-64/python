print("enter size of l1")
a=int(input())
list1=[]
list2=[]
list3=[]

for i in range(0,a):
    list1.append(int(input()))
    
print("enter size of l2")
a=int(input())
for i in range(0,a):
    list2.append(int(input()))
    
print("enter size of l3")
a=int(input())
for i in range(0,a):
    list3.append(int(input()))


def f1(x,y):
    return (x+y)
print(list(map(f1,list1,list3)))

def mul(x,y):
    return (x*y)
print(list(map(mul,list1,list3)))


def c(x,y):
    if(x==y):
        return x
    else:
        return (x,y)

print(list(map(c,list1,list2)))

def diff(x,y):
    if(x!=y):
        return (x,y)
    else:
        return x

print(list(map(diff,list1,list2)))

