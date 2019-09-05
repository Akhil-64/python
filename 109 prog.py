import random
print("times of dice thrown")
a=int(input())
list1=[]
list2=[]
dict1={}
q=0
count2=0
count3=0
count4=0
count5=0
count6=0
count7=0
count8=0
count9=0
count10=0
count11=0
count12=0
for i in range(0,a):
    print("dice",i+1,":")
    a=random.randint(1,6)
    b=random.randint(1,6)
    print(a)
    print(b)
    q=a+b
    print("sum:",q)

    list1.append(q)
    if(q==2):
        count2+=1
    if(q==3):
        count3+=1
    if(q==4):
        count4+=1
    if(q==5):
        count5+=1
    if(q==6):
        count6+=1
    if(q==7):
        count7+=1
    if(q==8):
        count8+=1
    if(q==9):
        count9+=1
    if(q==10):
        count10+=1
    if(q==11):
        count11+=1
    if(q==12):
        count12+=1
#print(list1)
for j in list1:
  if  j not in list2:
      list2.append(j)
#print(list2)
for i in list2:
 if(i==2):
        print("2 count=",count2)
 if(i==3):
        print("3 count=",count3)
 if(i==4):
        print("4 count=",count4)
 if(i==5):
       print("5 count=",count5)
 if(i==6): 
       print("6 count=",count6)
 if(i==7):
        print("7 count=",count7)
 if(i==8):
        print("8 count=",count8)
 if(i==9):
        print("9 count=",count9)
 if(i==10):
        print("10 count=",count10)
 if(i==11):
        print("11 count=",count11)
 if(i==12):
        print("12 count=",count12)

