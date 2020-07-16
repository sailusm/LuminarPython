f=open("C:/Users/USER/PycharmProjects/project1/flowcotrol/file/movies.csv","r")
dic={}
r=[]
m=[]
for i in f:
       # print(i)
       words=i.rstrip("\n").split(",")
       # print(words)
       rate=words[3]
       r.append(rate)
       movie=words[1]
       m.append(movie)
       if(rate not in dic):
            dic[rate]=1
       else:
            dic[rate]+=1
       # if (movie not in dic):
       #     dic[movie] = 1
       # else:
       #     dic[movie] += 1
#print(dic)
print(r)
# print(m)
# max=(max(r))


# for q,w in dic.items():
#      print(q,w)