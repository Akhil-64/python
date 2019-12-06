ra=int(input())
list1=[]
list2=[]
'''for i in range(0,ra,2):
    list1.append(int(input()))
    list2.append(int(input()))

'''
list3=[]
for i in range(0,ra):
    list3.append(int(input()))
list4=[]
for i in range(0,len(list3)-1,2):
    list4.append((list3[i+1],list3[i]))

print(list4)
                 
