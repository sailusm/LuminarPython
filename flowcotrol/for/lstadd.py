lst=[1,2,3,4,5,6,7,8]
print (lst)
element=int(input("enter a num"))
for num in lst:
    for i in lst:
        if(num+i==element):
            print(num,i)