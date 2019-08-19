print("dict1 m to cm")
list1=[]
list2=[]
for key in range(20,233):
    list1.append(key)
    list2.append(key)
dict2=dict(zip(list1,list2))


dict1={k:v*100 for (k,v) in dict2.items()}
print(dict1)



print("dict2 cm to m")
list3=[]
list4=[]
sum2=0
for key in range(20,233):
    list3.append(key)
    list4.append(key)
d1=dict(zip(list3,list4))
d2={k:v/100 for (k,v) in d1.items()}
print(d2)

