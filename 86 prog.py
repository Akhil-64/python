print("enter dictionary size")
a=int(input())
list1=[]
list2=[]
dict1={}
for i in range(0,a):
    print("enter key")
    key=input()
    print("enter value")
    value=input()
    list1.append(key)
    list2.append(value)
    dict1[key]=value
print(dict1)
print("actual dictionary",dict(zip(list1,list2)))
print("inverted dictionary",dict(zip(list2,list1)))
