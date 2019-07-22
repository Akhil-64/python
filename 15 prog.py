print("enter sal")
a=int(input())
print("enter gender")
b=str(input())
if(b=='male'):
    if(a<10000):
       c=(a*0.05)+(a*0.02)+a
       print("bonus for male is",c)
    else:
       d=(a*0.05)+a
       print("bonus for female is",d)
else:
    if(a<10000):
        cd=(a*0.10)+(a*0.02)+a
        print("bonus for female is",cd)
    else:
        de=(a*0.10)+a
        print("bonus for female is",de)
