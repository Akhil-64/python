print("enter name")
name=input()
print("enter dob with spaces")
dob=input()
a=dob.split(" ")
print("enter today's date")
date=input()
b=date.split(" ")

class person:
    def __init__(self,name,dob):
        self.name=name
        self.dob=dob
    def myfunc(abc):
        d=abs(int(a[2])-int(b[2]))
        print(d)
        if d>18:
            print("eligible")
        elif d==18:
            if b[1]<a[1]:
                print("not eligible")
            else:
                if b[0]<a[0]:
                  print("not eligible")
                else:
                    print("eligible")
        else:
            print("not")
p1=person(name,dob)
p1.myfunc()

    
        
