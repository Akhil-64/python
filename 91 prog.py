print("enter 2 numbers")
n1=int(input())
r1=int(input())
def factorial(n,r):
    fact=1
    fact2=1
    for i in range(1,n+1):
        fact=fact*i;
    diff=n-r
    for j in range(1,diff+1):
        fact2=fact2*j
    res=fact//fact2
    return res



print(factorial(n1,r1))
