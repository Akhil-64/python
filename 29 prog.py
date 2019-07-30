print("enter number")
a=int(input())
if(a>0):
    for i in range(0,a):
        if(a%2==0):
            a=a/2
    if(a==1):
        print("number is prime number")
if(a==0 or a!=1):
    print("number is not prime")
        
        
