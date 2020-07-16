num=int(input("Enter a number:"))
re=0
while(num>0):
    dig=num%10
    re=re+(dig**3)
    num=num//10
print(re)