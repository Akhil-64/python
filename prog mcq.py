#1
doc=dict()
for  x in enumerate(range(2)):
    doc[x[0]]=x[1]
    doc[x[1]+5]=x[0]
print(doc)
i=1
#2
tup=["1",2,3,4,"2,3"]
tic={}
toc=tic
for z in tup:
    tic[z]=tic
    tic=tic[z]
print(toc)


