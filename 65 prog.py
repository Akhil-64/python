import random
fo=open("65 prog.py","r")
print("enter number")
a=int(input())
print("list is")
list1=[]
for i  in range(0,a):
    x=random.randint(0,a)
    list1.append(x)
print(list1)
b=random.choice(list1)
print(b)
flag=0
if (b>1):
  for i in range(2,b):
    if(b%i==0):
        flag=0
        break
  else:
    flag=1
elif(b==0 or b==1):
    flag=0
    
if(flag==1):
    fo.close()
else:
   print("non prime")
