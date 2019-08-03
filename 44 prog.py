print("enter string")
a1=str(input())
print("enter character")
b1=str(input())
a=a1.lower()
b=b1.lower()
count=0
for i in range(0,len(a)):
    if(a[i]==b):
        count+=1
if(count>0):
    print("character found")
    print("count=",count)
else:
    print("character not found")
    print("count=0")
