print("squares")
l1=[x**2 for x in range(1,10)]
s1=set(l1)
print(s1)
print("cubes")
l2=[x**3 for x in range(1,10)]
s2=set(l2)
print(s2)
print("update")
s1.update(s2)
print(s1)
print("pop")
print("pop s1")
s1.pop()
print(s1)
print("pop s2")
s2.pop()
print(s2)
print("remove")
print("remove s1")
s1.remove(512)
print(s1)
print("remove s2")
s2.remove(125)
print(s2)
print("add in s1")
s1.add("akhil")
print(s1)
print("add in s2")
s2.add(2)
print(s2)
print("clear s1")
s1.clear()
print(s1)
print("clear s2")
s2.clear()
print(s2)

