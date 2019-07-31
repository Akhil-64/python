print("enter user name")
a=str(input())
print("enter pan card number")
b=str(input())
cd=b.isalnum()
if(cd==True):
    print(a)
    print(b)
else:
    print("invalid details")
