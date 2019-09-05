import math 
print("enter number")
a=int(input())
list1=[]
def squarefree(n):
    if n%2==0:
        n=n/2
    if n%2==0:
        return False
    for i in range(3,int(math.sqrt(n)+1)):
        if(n%i==0):
            n=n/i
        if n%i==0:
            return False
    return True
print(squarefree(a))
