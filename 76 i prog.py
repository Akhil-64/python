print("dictionary")
d1={'delhi':'dl','chandigarh':'ch','punjab':'pb'}
print("add")
print("enter key")
key=input()
print("enter value")
value=input()
d1[key]=value
print(d1)
print("enter the key you want to search")
key1=input()
if key1 not in d1:
    print("SORRY! no idea")
else:
    print(d1)
