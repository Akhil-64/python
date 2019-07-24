print("enter no")
a=int(input())
i=0
count=0
sum1=0
print("reverse of the nos")
while(a>0):
    b=int(a%10)
    print(b,end="")
    a=int(a/10)
    sum1=sum1+b
print("\n")
print("sum is:",sum1)
