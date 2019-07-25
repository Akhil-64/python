print("enter no")
a=int(input())
num=a
gh=len(str(a))
b=0
c=0
sum1=0
count=0
'''while(a>0):
    b=int(a%10)
    count+=1
    a=int(a/10)
a=int(input())'''
while(num>0):
    c=int(num%10)
   # print("rem",c)
    sum1=sum1+(c**gh)
    #print("sum",sum1)
    num=int(num/10)
   # print("A",a)   
if(sum1==a):
    print("armstrong number")
else:
    print("not an armstrog number")
    

    
    

