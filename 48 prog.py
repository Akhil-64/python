print("enter string")
a1=str(input())
a1=a1.split(",")
for i in range(len(a1)):
    j=i+1
    for j in range(len(a1)):
        if(a1[i]<a1[j]):
            temp=a1[i]
            a1[i]=a1[j]
            a1[j]=temp
print(",".join(a1))
