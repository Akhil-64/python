a=int(input())#size
list1=[]
list2=[]
for i in range(0,a):
    x=int(input())
    list1.append(x)
list4=[]
list4.extend(list1)
list1.reverse()
list2.extend(list1)
#print("reverse",list2)
#print("actual",list4)
sum1=0
list3=[]
list5=[]
for i in range(0,a):
    sum1=list4[i]+list2[i]
    print(sum1,end=" ")
  

'''a=int(input())
b=int(input())
if(a<b):
    print(a)
else:
    print(b)'''
