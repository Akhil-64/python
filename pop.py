dict1={'zk':'ak','sd':'f','ak':'z'}

dict2=sorted(dict1.keys())
print(dict2)
dict3=sorted(dict1.values())
print(dict3)

for key,value in sorted(dict1.items(),key=lambda item:item[1]):
    print("%s:%s" %(key,value))


print(dict1.get('zk'))
x=dict1.setdefault("ku","akhil")
print(x)
	
