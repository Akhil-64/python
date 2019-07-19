print("enter the marks of exam")
mark=int(input())
mark1=int(input())
print("enter the marks of sports")
mark2=int(input())
print("enter the marks of activities")
mark3=int(input())
mark4=int(input())
mark5=int(input())
exam=((mark+mark1)/200)*0.50
sports=(mark2/50)*0.20
activities=((mark3+mark4+mark5)/60)*0.30
ab=exam+sports+activities
abc=ab*100
print("student marks percentage:",abc,"%")

