print("enter string")
a1=str(input())
print("enter 2nd string")
b=str(input())
a=sorted(a1)
for i in range(0,len(a)):
    print(a[i]+b,end=" ")
    if((i+1)%3==0):
        print("\n")


