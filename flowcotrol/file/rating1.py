f=open("C:/Users/USER/PycharmProjects/project1/flowcotrol/file/movies.csv","r")
r=[]
m=[]
dic={}
count=0

for line in f:
       # if(count==5):
       #      break
       # else:
            words=line.rstrip("\n").split(",")
            rate=float(words[3])
            r.append(rate)
            movie=words[1]
            m.append(movie)
            count+=1

# for i in m:
    # for l in r:
            if(movie not in dic):
                dic[movie]=rate
            # count+=1
print(dic)
max=(max(r))
print("Highest Rating=>",max)
print("Movies With Highest Rating")
print("__________________________")
for x,y in dic.items():
     if(y==4.3):
         print(x)
#
#
#
