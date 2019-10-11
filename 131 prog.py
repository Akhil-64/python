print("enter string")
a=input()
class string():
    def __init__(self,st):
        self.st=st
    def upper(self):
        count=0
        for i in self.st:
            if(i>="A" and i<="Z"):
                count+=1
        print("upper:",count)
    def lower(self):
        count1=0
        for i in self.st:
            if(i>="a" and i<="z"):
                count1+=1
        print("lower:",count1)
    def spaces(self):
        count2=0
        for i in self.st:
            if (i==" "):
                count2+=1
        print("sapces:",count2)
    def vowels(self):
        count3=0
        for i in self.st:
            if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
                count3+=1
        print("vowels:",count3)
    def consonants(self):
        count4=0
        for i in self.st:
            if(i>="A" and i<="Z") or (i>="a" and i<="z"):
                count4+=1
                #print(i)
        print("consonants:",count4)
obj1=string(a)
obj1.upper()
obj1.lower()
obj1.spaces()
obj1.vowels()
obj1.consonants()

        
    
 
