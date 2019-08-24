print("size of dictionaries")
b=int(input())
print("enter number of keys and values")
a=int(input())
list1=[]
list2=[]
list3=[]
for i in range(0,b):
  print("dict",i)
  for j in range(0,a):
      print("enter key")
      key=input()
      print("enter value")
      value=input()
      list1.append(key)
      list2.append(value)
  d1=dict(zip(list1,list2))
  list3.append(d1)
  list1.clear()
  list2.clear()
print(list3)

len1=len(list3)
'''print(list3[0])
print(list3[len1-1])'''
if(b>1):
 for i in list3[0].values():
  i2=i
 print(i2)
 for j in list3[len1-1].values():
  j2=j
 print(j)
 sum1=int(i)+int(j)
 print(sum1)
 list4=[]
 list5=[]
 dict1=dict()
 '''for i in range(1,len1-1):
   for x2 in list3[i].values():
     print(x2)'''

 for i in range(1,len(list3)-1):
   
   for j in list3[i].values():
     #dict1[j]=value
     list4.append(j)
   for j2 in list3[i].values():
     list5.append(j2)
 #dict1.setdefault(i," ").append(j)
     dict1.setdefault(j2,j)
     break
 
 for i in list3[0].values():
    print("{",i,":",sum1,"}",dict1)
    break
 
   

 

     
 
else:
 for i in list3[0].values():
  print(i)
  
  
