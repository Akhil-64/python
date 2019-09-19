import re
p="akhil hello world ak akhil"
x=re.findall("^hello",p)
if (x):
    print("yes")
else:
    print("no")
y=re.findall("world$",p)
if(x):
    print("ohk")
else:
    print("no")
y=re.findall("he..o",p)
print(y)
y=re.findall("[a-m]",p)
print(y)
y=re.findall("[a-k]",p)
print(y)
y=re.findall("[^a]",p)
print(y)
y=re.findall("akx*",p)
print(y)
if (y):
    print("found")
else:
    print("not found")
y=re.findall("akx+",p)
print(y)
if(y):
    print("found")
else:
    print("not found")
y=re.findall("hel{2}o",p)
print(y)
