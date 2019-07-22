print("enter number:")
a=int(input())
b=int(input())
c=int(input())
print("enter from user numbers are:")
if(a>b and a>c):
    print(a)
elif(b>a and b>c):
    print(b)
else:
    print(c)

if(b>a and b<c)or(b<a and b>c):
    print(b)
elif(a>b and a<c)or(a<b and a>c):
    print(a)
else:
    print(c)

           
if(a<b and a<c):
    print(a)
elif(b<a and b<c):
    print(b)
else:
    print(c)
    
    
if(a>b and a>c):
    print("largest number is:",a)
elif(b>a and b>c):
    print("largest number is:",b)
else:
    print("largest number is:",c)

