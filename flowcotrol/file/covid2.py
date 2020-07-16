f=open("C:/Users/USER/PycharmProjects/project1/flowcotrol/file/complete.csv","r")
i=0
dict={}
for lines in f:
    report=lines.rstrip("\n").split(",")
    state=report[1]
    cases=int(report[4])
    if(state not in dict):
        dict[state]=cases
    else:
        dict[state]=cases
print(dict)
import matplotlib.pyplot as plt
states=[]
cnt=[]
for k,v in dict.items():
    states.append(k)
    cnt.append(v)
    plt.bar(states,cnt)
plt.show()

