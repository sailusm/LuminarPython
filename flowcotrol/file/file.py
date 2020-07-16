f=open("C:/Users/USER/PycharmProjects/project1/flowcotrol/file/movies.csv","r")
dic={}
for i in f:
       # print(i)
       words=i.rstrip("\n").split(",")
       # print(words)
       year=words[2]
       if(year not in dic):
            dic[year]=1
       else:
            dic[year]+=1
#print(dic)
print(words)
# for q,w in dic.items():
#      print(q,w)