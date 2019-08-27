print("enter string")
a=input()
def panagram(a1):
    a2=a1.lower()
    count=0
    list4=[]
    for i in a2:
        if i not in list4:
            list4.append(i)
    #print(list4)
    list4.remove(" ")
    #count=len(list4)
    #print(list4)
    for i in range(0,len(list4)):
        if (ord(list4[i])>=97 and ord(list4[i])<=122):
            #print(a[i])
            count+=1
            #print(count)
        else:
            continue
    #print(count)
    if(count==26):
        print("panagram")
        
    else:
        print("not")


panagram(a)
