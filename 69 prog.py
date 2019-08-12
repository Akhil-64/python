print("enter string")
a=str(input())
b=a.split(",")
#print(b)
#print(b[1])

for i in range(0,len(b)):
     ab=int(b[i],2)
     if(ab%5==0):
         print(bin(ab),end=",")
  
'''print()
for i in range(0,len(b)):
     x=(b[i][i]*(2**i))'''
