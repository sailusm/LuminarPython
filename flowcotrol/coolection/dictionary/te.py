k=["g","f"]
j=[1,2]
dic={}
count=0


for i in k:
    for l in j:
        if(i not in dic):
            dic[i]=j[count]
            count+=1
print(dic)
for x,y in dic.items():
    if(y==2):
        print(x)