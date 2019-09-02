list1=[]
for i in range(1,20):
    list1.append(i)
print(list1)
print(list(filter(lambda x:x%2==0 or x%4==0,list1)))
