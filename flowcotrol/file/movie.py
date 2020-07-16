f=open("C:/Users/USER/PycharmProjects/project1/flowcotrol/file/movies","r")
dic={}
for i in f:
       # print(i)
       words=i.rstrip("\n").split(" ")
       # print(words)
       for j in words:
        if(j not in dic):
               dic[j]=1
        else:
               dic[j]=dic[j]+1
print(dic)
for q,w in dic.items():
    print(q,w)