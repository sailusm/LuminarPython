lst=[1,4,5,8,9,6,3,9,2]
lst.sort()
print(lst)
val=int(input("enter value"))
for i in lst:
    low = 0
    upper = len(lst) - 1

    res=lst[low]+lst[upper]
    if(res==val):
        print((lst[low],lst[upper]))
        low+=1

        break

    elif(res>val):
        upper=upper-1
    elif(res<val):
        low=low+1
    else:
        low+=1
    print(upper)
    

