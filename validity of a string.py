print("enter string")
a=input()
print("validity:")
for i in range(0,len(a)):
    b=a.count("{")
    c=a.count("}")
    d=a.count("[")
    e=a.count("]")
    f=a.count("(")
    g=a.count(")")
if((b==c) and (d==e) and(f==g)):
    print("valid")
else:
    print("not valid")
        
