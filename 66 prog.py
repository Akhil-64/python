print("enter string")
a=str(input())
print("enter n")
n=int(input())
print("enter m")
m=int(input())
if(len(a)>2):
    for i in range(0,m):
         print(a[0:m]*3,end="")
        
else:
    print(a*n)
    
