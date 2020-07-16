num=int(input("enter range"))
flag=0
for i in range(2,num):
    if(num%i==0):
        flag=0
        break
    else:
        flag=1
if(flag==1):
    print("prime")
else:
    print("not")