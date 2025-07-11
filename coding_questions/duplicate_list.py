l=[1,2,3,4,4,5,3]
for i in l:
    x=l.count(i)
if x>=2:
    print("Duplicate Found at : ",l.index(i))