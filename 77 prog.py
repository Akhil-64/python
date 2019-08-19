i=0
dict1=dict()
sum1=0
list1=[]
list2=[]
print("enter radius")
while(i!=-1):
     i=int(input())
     
     if(i==-1):
         break
     else:
        list1.append(i)
        sum1=int(2*3.14*i)
        list2.append(sum1)
print(dict(zip(list1,list2)))
