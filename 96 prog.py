print("enter list size")
a=int(input())

def sum1(a1):
    list1=[]
    for i in range(0,a1):
        x=int(input())
        list1.append(x)
    return (sum(list1))
print(sum1(a))
