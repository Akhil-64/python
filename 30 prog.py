print("leap yrs between 1900 and 2101")
for i in range(1900,2101):
    if i%4==0 and(i%400==0 or i%100!=0):
       print(i,end=" ")
    else:
        continue
    
