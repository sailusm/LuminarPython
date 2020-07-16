f=open("C:/Users/USER/PycharmProjects/project1/flowcotrol/file/person")
emp={}
key={}
for lines in f:

    words=lines.rstrip("\n").split(",")
    key=words[0]
    if(lines not in emp):
        emp[key]=words
print(emp)



#     print(key)


        # for i in lines:
        #     print(i)
            # count=0
            # if(count==1):
            #     break
            #     print(i)
            #     count+=1
            #
            #     # emp[lines]

# print(emp)

