print("gcd by euclid's algorithm")
a=int(input())
b=int(input())
while(b!=0):
    gcd=b
    b=a%b
    a=gcd
print(gcd)

        
