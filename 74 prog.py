print("even nos")
list1=[x for x in range(1,10) if(x%2==0)]
s1=set(list1)
print(s1)
list2=[]
list3=[]
print("composite number")
for x in range(1,20):
    if(x>1):
        for i  in range(2,x):
            if(x%i==0):
                list2.append(x)
                break
        else:
            list3.append(x)
    else:
        list2.append(x)
s2=set(list2)
print(s2)
x2=all(s1)
print(x2)
x3=all(s2)
print(x3)
x4=s1.issuperset(s2)
print(x4)
print(len(s1))
print(len(s2))
print(sum(s1))
print(sum(s2))

            
