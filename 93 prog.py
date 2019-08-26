print("enter values")
a=input()
b=input()
def var_length(*length):
    '''for i in length:
        print(i)'''
    return length
print(var_length(a,b))
print(var_length.__doc__)
