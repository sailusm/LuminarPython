lst=[5,2,4,3,1,6,7,8,9,10]
lst.sort()
print(lst)
low=0
upper=len(lst)-1
search=int(input("enter the number to find it out"))
flag=0
while(low<upper):
    mid=low+upper//2
    if(search>lst[mid]):
        low=mid+1
    elif(search==lst[mid]):
        flag=1
        break
    elif(search<lst[mid]):
        upper=mid-1
if(flag==1):
    print("found")
else:
    print("not founs")