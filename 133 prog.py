print("enter money you want to deposit")
a=int(input())
print("enter money you want to withdrawal")
b=int(input())
class bank:
    def __init__(self,dep,wi):
        self.dep=dep
        self.wi=wi
    
    def deposit(self):
        print("amount you deposited")
        print(self.dep)
       
        
    def withdrawal(self):
        print("amount you want to withdrawal")
        print(self.wi)
        
        
    def inquiry(self):
        if(self.dep<self.wi):
            print("not enough cash")
            print("balance available is:",self.dep)
        else:
            print("enough cash")
            print("balance available is:",self.dep-self.wi)
obj1=bank(a,b)
obj1.deposit()
obj1.withdrawal()
obj1.inquiry()
    
