print("enter size")
a=int(input())
list1=[]
print("enter list")
for i in range(0,a):
    x=int(input())
    list1.append(x)
print(list1)
print("enter character")
n=input()
for i in range(0,a):
    for j in range(0,list1[i]):
      print("$",end="")
    print()
