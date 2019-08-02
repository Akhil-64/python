a="akhil is good"
b=a.capitalize()
print(b)
c=a.center(20,'0')
print(c)

d="apple apple a day apples"
e=d.count("apple",4,12)
print(e)
f=d.endswith("apples")
print(f)
g=d.endswith("appl",3,10)
print(g)
h=d.startswith("apple",0,3)
print(h)

ab="hello world by python"
cd=ab.find("oll",14)
print(cd)
fg=ab.index("ll")
print(fg)
df=ab.rfind("l")
print(df)
q=ab.rindex("o")
print(q)
df="123"
print(df.isalnum())
print(ab.isalnum())
print(df.isalpha())
print(df.isdigit())
k="aj DJ kjjfbu rhnir"
print(k.islower())
print(k.isupper())
k1="  " 
print(k1.isspace())
print(len(k))
k2=("akhil","kumar")
print("len is",len(k1))

dict1={"type":"fruit","category":"apple","allp":"joe"}
print(len(dict1))
print(k.rjust(20,'0'))

x="abc abc ab12 12abc"
print(x.rstrip("abc12 "))
y="..ddd.....''''flf"
print(y.lstrip(".d'"))
df="abc ab12"
print(df.lstrip("abc "))
print(df.upper())
print(df.lower())
print(df.zfill(10))
print(max(df))
print(df.replace("abc","akhil"))
print(x.replace("abc","",2))
print(x.swapcase())
print(x.split(" ",2))
ak=("akhil","kumar")
print("#".join(ak))
if(x>y):
    print("yes")
else:
    print("false")
