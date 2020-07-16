r1=int(input("enter a arange"))
r2=int(input("enter a 2nd arange"))
sum=0
s=0
while(r1<=r2):
    if(r1%2==0):
        sum=sum+r1

    else:
        s=s+r1
    r1+=1
print(sum)
print(s)
