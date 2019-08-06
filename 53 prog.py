print("enter size")
a=int(input())
print("enter list")
list1=list()
list2=list()
for i in range(0,a):
    b=input()
    list1.append(b)
print("using sort ascending order")
for i in range(0,a):
    list1.sort()
print(list1)
print("using sort descending order")
for i in range(0,a):
    list1.sort(reverse=True)
print(list1)

print("using sorted ascending order")
for j in range(0,a):
    list2=sorted(list1)
print(list2)

print("using sorted descending order")
for j in range(0,a):
    list2=sorted (list1,reverse=True)
print(list2)
