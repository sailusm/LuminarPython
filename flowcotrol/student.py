name=input("enter a name")
mark1=int(input("enter a mark1"))
mark2=int(input("enter a mark2"))
mark3=int(input("enter a mark3"))
total=mark1+mark2+mark3
print("Total is",total)
if(total>=145):
    print(name," your grade is A+")
elif(total>140)&(total<145):
    print(name," your grade is A")
elif(total>135)&(total<140):
    print(name," your grade is B")
elif(total<130):
    print(name,"you failed")
# else:
#     print("valid marks")