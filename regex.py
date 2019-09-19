import re
pattern="she"
r1="she sells sea shells on the sea shore"
if re.match(pattern,r1):
    print("match")
else:
    print("not found")

x=re.match(pattern,r1)
print(x)

r2="python java"
p="java"
if(re.search(p,r2)):
    print("yes")
else:
    print("no")

r3="python java pytorch"
x=re.sub("py","jy",r3,1)
print(x)

r4="akhil kumar akhil kumar"
p="ak"
x2=re.findall(p,r4)
print(x2)

r5="akhil kumar"
p="ak"
x3=re.finditer(p,r5)
print(x3)


