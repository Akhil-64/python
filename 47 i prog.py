print("enter string")
a=str(input())
print(a[len(a)-1],end="")
for i in range(1,len(a)-1):
    print(a[i],end="")
print(a[0])
