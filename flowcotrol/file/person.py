f=open("C:/Users/USER/PycharmProjects/project1/flowcotrol/file/person","r")
dict={}
for line in f:
    words=line.rstrip("\n").split(",")
    id=words[0]
    name=[words[2]]
    desi = [words[4]]
    salary = [words[6]]
    if id not in dict:
        dict[id]={"id":id,"name":name,"desi":desi,"salary":salary}
# for k,v in dict.items():
    # print(k,v)
def employee(**args):
    id=args["id"]
    prop=args["property"]
    print(dict[id]["name"],end="")
    print(dict[id][prop])


employee(id="300",property="desi")
















