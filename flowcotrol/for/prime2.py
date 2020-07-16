num=int(input("enter a limit"))
num2=int(input("enter a limit2"))
flag=0
for i in range(num,num2+1):
    for j in range(1,num):
        if(num%j==0):
            flag=0
            break
        else:
            flag=1
            break
        if(flag==1):
            print(num)
    # num+=1
