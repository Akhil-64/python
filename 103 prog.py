from functools import reduce
print("enter size")
a=int(input())
l1=[]
for i in range(0,a):
     l1.append(int(input()))
print(l1)
print(reduce(lambda x,y:x if x>y else y,l1)) 
