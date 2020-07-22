f=open("emp")
for line in f:
    vname=line.rstrip("\n").split(",")
    email=vname[3]
    # print(email)


    import re
    x='[a-zA-Z]\w*@gmail[.]com'
    # vname=input("enter a name")
    match=re.fullmatch(x,email)
    if(match!=None):
        f1=open("validmail",'a')
        f1.write(email)
        f1.write("\n")
        print(email)
        # print("valid")
    # else:
    #     f2=open("invalid",'a')
    #     f2.write(email)
    #     f2.write(", ")
    #     # print("invalid")