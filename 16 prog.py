print("enter year")
a=int(input())
if(a%4==0 or a%400==0 or a%100==0):
    print("leap yrs")
else:
    print("not a leap yr")
