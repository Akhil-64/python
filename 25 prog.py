print("enter characters")
a=0
count=0
count2=0
while(a!="*"):
    a=str(input())
    if(a>='a' and a<='z'):
        count+=1
    elif(a>='A' and a<='Z'):
        count2+=1
print("upper case",count2)
print("lower case",count)
