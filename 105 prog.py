from functools import reduce
l1=[10,20,30,40]
l2=[50,60,70,80]
l1.extend(l2)
print(l1)
print(reduce(lambda x,y:x+y,l1))
