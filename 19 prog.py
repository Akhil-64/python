print("enter income")
sal=int(input())
if(sal<=150000):
    print("no tax")
else:
    tax_income=sal-150000
    if(tax_income<=150000):
        a=(tax_income*0.10)
        print("tax is:",a)
    elif(tax_income>150000):
        t1=(150000*0.10)
         
        b=tax_income-150000
       
        if(b<=200000):
            t2=b*0.20
            d=t1+t2
            print("tax is",d)
        elif(b>200000):
            t3=(200000*0.20)
            c=b-200000
            f=(c*0.30)
            t4=t1+t3+f
            print("total tax is:",t4)
        

