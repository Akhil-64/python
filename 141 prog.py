print("enter title name")
title=input()
print("enter publisher")
publisher=input()
print("enter price")
price=int(input())
print("enter title name")
title1=input()
print("enter publisher")
publisher1=input()
print("enter price")
price1=int(input())
class book:
    def __init__(self,t,p,pr):
        self.t=0
        self.p=0
        self.pr=0
        
    def set(self,t,p,pr):
        self.t=t
        self.p=p
        self.pr=pr
        
    def __lt__(self,other):
        if (self.pr<other.pr):
            return "price of book 1 is less"
        else:
            return "price of book 2 is less"
    def __gt__(self,other):
        if (self.pr>other.pr):
            return "price of book 1 is greater"
        else:
            return "price of book 2 is greater"
    def __eq__(self,other):
        if (self.pr==other.pr):
            return "price of books are equal"
        else:
            return "price of books are not equal"
        
    def display(self):
        print("title is:",self.t)
        print("publisher name is:",self.p)





obj1=book(title,publisher,price)
obj1.set(title,publisher,price)
obj2=book(title1,publisher1,price1)
obj2.set(title1,publisher1,price1)
obj1.display()
obj2.display()
print(obj1<obj2)
print(obj1>obj2)
print(obj1==obj2)








