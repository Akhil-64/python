print("enter string")
a=input()
print("enter 1st character")
b=input()
print("enter 2nd character")
c=input()
count=0

for i in range(0,a.find(c)+2):
    for j in range(0,i):
        print(a[j],end=" ")
    count+=1
    print()
print(count-1)            
         
