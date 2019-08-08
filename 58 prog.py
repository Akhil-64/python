print("enter list")
print("enter size of matrix")
a=int(input())
list2=[]
list1=[]
list4=[]

for i in range(0,a):
    list1=[]
    for j in range(0,a):
        list1.append(int(input()))
    list2.append(list1)
print(list2)
print("matrix1")
for i in range(0,a):
    for j in range(0,a):
        print(list2[i][j],end=" ")
    print()
print("enter elements of 2ns matrix")
for k in range(0,a):
    list3=[]
    for l in range(0,a):
        list3.append(int(input()))
    list4.append(list3)
print(list4)
print("matrix2")
for i in range(0,a):
    for j in range(0,a):
        print(list4[i][j],end=" ")
    print()
print("list 6 is ")    
list6=[]
for i in range(0,a):
    list5=[]
    for j in range(0,a):
        list5.append(0)
    list6.append(list5)
print(list6)
print("matrix 3")
for i in range(0,a):
    for j in range(0,a):
        print(list6[i][j],end=" ")
    print()

for i in range(a):
    for j in range(a):
                   list6[i][j]=list2[i][j]+list4[i][j]
print(list6)
for i in range(a):
    for j in range(a):
        print(list6[i][j],end=" ")
    print()
    
print("resultant matrix is")
for i  in list6:
    print(i)
     
