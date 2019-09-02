print("enter string")
a=input()
def vowel(n):
    if(n=="a" or n=="e" or n=="i" or n=="o" or n=="u"):
        return True
    else:
        return False
        
f1=filter(vowel,a)
print(list(f1))

#another way

#print(list(filter(lambda n:n=="a" or n=="e" or n=="i" or n=="o" or n=="u",a)))
