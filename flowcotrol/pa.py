lst=[]
l=int(input("enter len"))
k=int(input("enter elements"))
for m in range(0,l):
    k=int(input())
    lst.append(k)

s=sum(lst)
ls=[]
print(lst)
count=0
for j in lst:
    if(lst[count])==j:
            to=s-j
            ls.append(to)
            count+=1
print(ls)
