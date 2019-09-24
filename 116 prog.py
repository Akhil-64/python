import re
print("enter string")
x=input()
p="\w$"
a=re.findall(p,x)
#print(a)
p2="\w\B"
c=re.findall(p2,x)
#print(c)
d=" "
for i in c:
    d=d+i
#print(d)
p3="\w$"
b=re.findall(p3,d)
#print(b)
for i in a:
    print(i)
for i2 in b:
    print(i2)
if(i=="y"):
    print(re.sub(i,"ies",x))
elif(i=="o" or i=="x" or i=="z" or i=="s"):
    print(x+"es")
elif((i=="h" and i2=="c") or (i=="h" or i2=="s")):
    print(x+"es")
else:
    print(x+"s")

