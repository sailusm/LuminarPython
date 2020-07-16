st="abab"
wrd=[]
dic=[]
count = 0
for i in st:
    wrd.append(i)
    # print(wrd)
    if(i not in dic):
        dic.append(wrd[count])
        count += 1
    else:
        print(i)
        break
