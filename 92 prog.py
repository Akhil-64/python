print("size of series")
n=int(input())
def sum1(n1):
    res=0
    for i in range(0,n1):
        a=int(input())
        b=int(input())
        fact=1
        for j in range(1,b+1):
       
           fact=fact*j
           #print("fact",fact)
           #print("j",j)
        #print("fact",fact)
        res+=a/fact
    return res
     
     



print(sum1(n))

    
