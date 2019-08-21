print("enter size")
a=int(input())
print("enter dict1")
list1=[]
list2=[]
d1=dict()
for i in range(0,a):
    print("enter key")
    key=input()
    list1.append(key)
    print("enter value")
    value=input()
    list2.append(value)
    
d1=dict(zip(list1,list2))


print("enter dict2")
list3=[]
list4=[]
d2=dict()
for i in range(0,a):
    print("enter key")
    key1=input()
    print("enter value")
    value1=input()
    list3.append(key1)
    list4.append(value1)
d2=dict(zip(list3,list4))
print(d1)
print(d2)
list5=[]
list6=[]
for i in d1:
    print(i)
    list5.append(i)
for j in d2.values():
    print(j)
    list6.append(j)
print(dict(zip(list5,list6)))

