lst=[0,-1,2,3]
lst.sort()
low=-1
upper=len(lst)-1


while(low<=upper):
     if(low+1==upper):
         break
     low = low + 1
     for i in range(lst[low]+1,lst[low+1]):
             print (i)








