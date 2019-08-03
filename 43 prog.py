print("enter string")
a=str(input())
print("enter character")
b=str(input())
flag=0
count=0
#print("using index",a.index(b))
for i in range(0,len(a)):
    if(a[i]==b):
        count+=1
        flag=1
        break;
    else:
        flag=0
        count+=1
if(flag==1):
    print("without using index",count-1)
else:
    print("substring not found")

    




    

