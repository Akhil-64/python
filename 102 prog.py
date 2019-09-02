print("enter string")
a=input()
l1=list(map(lambda x:x.lower(),a))
for i in l1:
    print(i,end="")
