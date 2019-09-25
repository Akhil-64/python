import re
print("enter number")
x=int(input())
for i in range(0,x):
  print("enter name and email id")
  a=input()
  b=a.split()
  p="^[a-zA-Z][\w\.\-]+\@[a-zA-Z]+\.[a-zA-Z]{1,3}$"
  x2=re.findall(p,b[1])
  print(x2)
  if x2:
      print("valid e-mail")
  else:
      print("invalid e-mail")
  
  
