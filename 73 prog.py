print("set of odd numbers")

list1=[x for x in range(1,20) if(x%2!=0)]
print(list1)
s1=set(list1)
print(s1)
print("set of prime numbers")
list2=[]
list2=[x for x in range(2,20) if all((x%y!=0) for y in range(2,x))]
print(list2)
s2=set(list2)
print(s2)
print("union")
s3=s1.union(s2)
print(s3)
print("intersection")
s4=s1.intersection(s2)
print(s4)
print("difference")
s5=s1.difference(s2)
print(s5)
print("symetric difference")
s6=s1.symmetric_difference(s2)
print(s6)




                
