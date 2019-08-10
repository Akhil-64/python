print("input values")
list1=[]
for i in range(0,10):
    x=input()
    list1.append(x)
list2=[]
list3=[]
for i in range(0,10):
    if(i%2==0):
        list2.append(i)
    else:
        list3.append(i)
print("even list",list2)
print("odd list",list3)
