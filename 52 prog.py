print("enter size of list")
n=int(input())

list1=list()

for i in range(0,n):
    a=int(input())
    list1.append(a)

    
print("enter word you want to search")
x=int(input())
count=0
print("the index of word is: ")
for i in range(0,n):
    #print(list1.index(x))
    if(list1[i]==x):
        d=list1.index(x)
        print(d)
        count+=1
        list1[i]="$"
       
print("\ncount of ",x," is: ",count)
    
'''for i in range(0,n):
    if(list1[i]==x):
        count+=1
        break
print(count)'''
    
    

