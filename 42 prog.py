print("enter string")
a=str(input())
for i in
range(0,len(a)):
    if(a[i]=='a' or a[i]=='i' or a[i]=='o' or a[i]=='u' or a[i]=='e'):
        continue;
    else:
        print(a[i],end="")
