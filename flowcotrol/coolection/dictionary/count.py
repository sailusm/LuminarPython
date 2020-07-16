name="hari ,ravi,manu,ravi,manu,ram"
words=name.split(",")
print(words)
# print (words)
dict={}
for i in words:
    if(i not in dict):
        dict[i]=1
    else:
        dict[i]+=1
        print(dict)
        break

