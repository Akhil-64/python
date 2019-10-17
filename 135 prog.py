print("enter the number of persons")
a=int(input())
list1=[]
list2=[]
list3=[]
list4=[]
for i in range(0,a):
  print("enter name")
  name=input()
  print("enter book published")
  book=input()
  list1.append(name)
  list4.append(book)
#print(list1,list2,list3,list4)
class person:
    def __init__(self,l1,l2):
        self.l1=l1
        self.l2=l2
    def display(self):
        print("name of faculty :")
        for i in self.l1:
            print(i)
    def display2(self):
        print("name of books publications :")
        for i in self.l2:
            print(i)
class faculty(person):
    def __init__(self,l1,l2):
        person.__init__(self,l1,l2)
        
class publication(person):
    def __init__(self,l1,l2):
        person.__init__(self,l1,l2)
    
obj1=faculty(list1,list4)
obj1.display()
obj2=publication(list1,list4)
obj2.display2()

