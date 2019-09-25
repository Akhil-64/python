import re
print("enter number")
a=int(input())
flag=0
if(a>=2 and a<=15):
 for i in range(0,a):
    print("enter mobile number")
    x=input()
    if len(x)==10:
        p="^[789]\w+"
        x2=re.findall(p,x)
        print(x2)
        if x2:
             print("valid mobile number")
        else:
             print("invalid mobile number")
    else:
        print("invalid mobile number")
else:
    print("incorrect times")
    
