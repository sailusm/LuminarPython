f=open("C:/Users/USER/PycharmProjects/project1/flowcotrol/file/data.txt",""'r')
dict={}
lst=[]
lst2=[]
for line in f:
    # print(line)
    word=line.rstrip("\n").split(",")
    dist=word[0]
    tempr=int(word[1])
    # print(tempr)
    if dist not in dict:
        dict[dist]=tempr
    elif(tempr>dict[dist]):
         dict[dist]=tempr
print(dict)
# lst1=[]
# lst=[]
# lst.sort
#
#
# for k,v in dict.items():
#     lst.append((v,k))
#     lst1.append(k)
print(lst)


