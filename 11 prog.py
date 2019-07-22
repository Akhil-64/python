print("enter a number to convert it into hexadecimal")
a=int(input())
print("hexadeximal is:",end="")
i=0
a6=[]
while(a>0):
   rem3=int(a%16)
   if(rem3==10):
      rem3='a'
   elif(rem3==11):
      rem3="b"
   elif(rem3==12):
      rem3="c"
   elif(rem3==13):
      rem3="d"
   elif(rem3==14):
      rem3="e"
   elif(rem3==15):
      rem3="f"
   else:
      rem3
   a6.append(rem3)
   a=int(a/16)
   i+=1;
a6.reverse()
for b in a6:
   print(b,end="")
print("\n")
print("enter a number to convert it into octal")
a3=int(input())
print("\noctal is:")
i=0
a5=[]
while(a3>0):
    rem1=int(a3%8)
    a5.append(rem1)
    a3=a3//8
    i+=1;
a5.reverse()
for i in a5:
   print(i,end="")
    
print("\n")
print("enter a number to convert it into binary")
a2=int(input())
ab=[]
i=0
print("binary is:")
while(a2>0):
    rem=int(a2%2)
    ab.append(rem)
    a2=int(a2/2)
    i+=1
ab.reverse()
for x in ab:
   print(x,end="")
    
print("\n")
print("enter a binary number to convert it into decimal")
bin=list(str(input()))

bin2=0
i2=0
for i in reversed(bin):
   bin2+=(2**i2)*int(i)
   i2+=1
print("decimal is:",bin2)
print("\n")
print("enter a octal number to conver it into decimal")
oct1=list(str(input()))
x2=0
x3=0
for x in reversed(oct1):
         x3+=(8**x2)*int(x)
         x2+=1
print("decimal is:",x3)

   


   
   
   






