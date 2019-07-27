print("enter end number in series")
a=int(input())
sum1=0
for i in range(1,a+1):
 #   print("before:",i)
    sum1=sum1+(1/i**2)
    #print("after:",i)
print(sum1)    

