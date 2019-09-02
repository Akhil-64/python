print("enter size")
a=int(input())
l1=[]
l2=[]
l3=[]
print("enter list")
for i in range(0,a):
    x=input()
    l1.append(x)
    l3.append(x)
    
l2=list(map(lambda x:x[::-1],l1))
l4=[]
print(l2)
for i in range(0,len(l1)):
    if(l1[i]==l2[i]):
        l4.append("yes")
    else:
        l4.append("no")
print(l4)

#print(list(filter(lamdba i:i if i==
              
