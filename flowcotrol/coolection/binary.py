lst=[1, 2, 3, 5, 6, 7, 8,150,200]
lst.sort()
print(lst)
low=0
upper=len(lst)
element=int(input("enter the element you want to search"))
flag=0
count = 0
while(low<upper):
    count+=1
    if (count>len(lst)):
       break
    mid = (low + upper) // 2  # first value a 3
    if (element<lst[mid]):
       upper = mid
    elif(element==lst[mid]):
       flag = 1
       break
    elif(element>lst[mid]):
       low = mid
if(flag==1):
    print("found")
else:
    print("not found")
