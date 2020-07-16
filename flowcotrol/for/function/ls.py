lst=[1,6,7,2,4,5,6,6]
element=int(input("enter element for searching"))
flag=0
for num in lst:
    if (element==num):
        flag=1
        break
    else:
        pass
if(flag>0):
    print("it is present")
else:
    print("it is not present")

