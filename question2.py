ra=int(input())
list1=[]
print("enter list")
for i in range(0,ra):
    list1.append(input())
print("enter string")
st=input()
list2=[]
for i in list1:
    list2.append(st+i)
print(list2)
