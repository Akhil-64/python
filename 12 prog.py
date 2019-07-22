print("enter age:")
a=int(input())
b=18-a
if(b>0):
    print("not eligible to vote by",abs(b))
else:
    print("eligible to vote")
