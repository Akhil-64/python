print("enter list1")
a=int(input())
list1=[]
list2=[]
print("enter list1")
for i in range(0,a):
    x=int(input())
    list1.append(x)
print("enter list2")
for i in range(0,a):
    y=int(input())
    list2.append(y)
print(list1)
print(list2)

list3=list1*2
for x1 in range(0,len(list1)):
    z=0
    for y in range(x1,x1+len(list1)):
        if(list2[z]==list3[y]):
            z+=1
        else:
            break
    if(z==len(list1)):
        print("identical")
    
        

   

