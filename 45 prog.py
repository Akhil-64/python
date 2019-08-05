print("enter string")
a=str(input())
b={}
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print('output string is:',b)
