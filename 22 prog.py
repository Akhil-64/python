print("enter no")
count=0
count1=0
count2=0
i=0
while(i!=-1):
    i=int(input())

    

    if(i>0):
      count+=1
    elif(i<0):
      count1+=1
    else:
      count2+=1

print("positive numbers are",count)
print("negative numbers are",count1)
print("zero numbers are",count2)
   
