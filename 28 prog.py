print("enter a number")
a=int(input())
if(a>1):
    for i in range(2,a):
        if(a%i)==0:
            print(a,"is composite")
            break
    else:
        print(a,"is prime")
            

else:
    print(a,"is composite")
