print("enter string")
a=str(input())
b=a.split(",")
for i in range(len(b)):
    j=i+1
    for j in range(len(b)):
        if(b[i]<b[j]):
            temp=b[i]
            b[i]=b[j]
            b[j]=temp
print(",".join(b))
