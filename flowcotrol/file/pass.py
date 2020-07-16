f=open("C:/Users/USER/PycharmProjects/project1/flowcotrol/file/students","r")
f1=open("C:/Users/USER/PycharmProjects/project1/flowcotrol/file\passed","r")

def readDataFromFile(fref):
    st=set()
    for data in fref:
        data=data.rstrip("\n")
        st.add(data)
    return st

st1=readDataFromFile(f)
st2=readDataFromFile(f1)
fail=st1-st2
# print(fail)