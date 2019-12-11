'''
a=input()
b=list(a)
c=[]
for i in b:
    if i not in c:
        c.append(i)
    else:
        c.append(i.replace(i,"$"))
for i in c:
    print(i,end="")
'''        
    

a=input()
b=a[0]
d=list(a)
c=[]
for i in d:
    if b not in c:
        c.append(b)
    else:
        c.append(i)

print(c)
        
    
    
    
