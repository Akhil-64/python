print("enter number")
a=int(input())
sum1=0
for i in range(0,a+1):
    if(i%2==0):
        sum1+=i
    else:
        continue
print(sum1)
