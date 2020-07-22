import functools
class employee:
    def __init__(self,eid,ename,mailid,salary):
        self.eid=eid
        self.ename=ename
        self.mailid=mailid
        self.salary=salary
    def printValues(self):
        print(self.eid,self.ename,self.mailid,salary)

lst=[]
lst2=[]
f=open("emp")
for line in f:
    # print(line)
    emp=line.rstrip("\n").split(",")
    eid=emp[0]
    ename=emp[1]
    mailid=emp[2]
    desig=emp[3]
    salary=emp[4]
    ob=employee(eid,ename,mailid,salary)
    lst.append(ob)
    k=list(map(lambda employee: employee.salary,lst))
    # print(k)
for i in k:
    lst2.append(i)
print(max(lst2))
    # ex = (functools.reduce(lambda a,b:a if a > b else b,lst, list(map(lambda employee:employee.salary,lst))))
    # print(ex)
    # print(salary)
