list1=[]
list2=[]
list3=[]
print("enter title")
title=input()
list1.append(title)
print("enter author")
author=input()
list2.append(author)
print("enter price")
price=input()
list3.append(price)
print("enter \"add book\" for enter a new book or enter \"display\" for display books")
option=input()

class book:
    def __init__(self,l1,l2,l3):
        self.l1=l1
        self.l2=l2
        self.l3=l3
    def read(self):
        self.l1=0
        self.l2=0
        self.l3=0
    def display(self):
        print("title of books:")
        for i in self.l1:
            print(i)
        print("author of books:")
        for j in self.l2:
            print(j)
        print("price of books:")
        for k in self.l3:
            print(k)

if option=="":
    print("DO you want to continue?")
    con=input()
    if (con=="yes"):
       print("enter title")
       title1=input()
       list1.append(title1)
       print("enter author")
       author1=input()
       list2.append(author1)
       print("enter price")
       price1=input()
       list3.append(price1)
    else:
        print("exit")
        
if (option=="add book"):
       print("enter title")
       title2=input()
       list1.append(title2)
       print("enter author")
       author2=input()
       list2.append(author2)
       print("enter price")
       price2=input()
       list3.append(price2)

obj1=book(list1,list2,list3)

if (option=="display"):
    obj1.display()
else:
    obj1.display()
        
    

