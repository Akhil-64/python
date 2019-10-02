try:
    print("enter number")
    x=input()
    if (x==""):
        raise KeyboardInterrupt("plz enter a number")
    print("enter denominator")
    y=int(input())
    x1=int(x)
    c=x1//y
    print(float(c))
#except KeyboardInterrupt:
#    print("plz enter a number")
except ZeroDivisionError :
    print("divide by zero error")
else:
    print("no error")
