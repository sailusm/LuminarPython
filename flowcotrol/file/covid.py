f=open("C:/Users/USER/PycharmProjects/project1/flowcotrol/file/complete.csv","r")
dict={}
for line in f:
    word=line.rstrip("\n").split(",")
    # print(word)
    country=word[1]
    state=int(word[4])
    if state not in dict:
        dict[state]= country
    else:
        dict[state]= country
# print(dict)
sortedlist=[]
for k,v in dict.items():g
     sortedlist.append((v,k))
print(sortedlist)

sortedlst=sorted(sortedlist,reverse=True)
print(sortedlst[1:4])

















