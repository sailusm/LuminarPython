lst=[5,2,4]
new=[]
count=1
for i in lst:
    k=i**count
    new.append(k)
    count+=1
print(new)