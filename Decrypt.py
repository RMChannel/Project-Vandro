import math
import os
file=open('d.png','wb')
file2=open('b','rb')
file3=open('c','rb')
data2=list(file2.read())
data3=list(file3.read())
i=0
data=[]
for i in data2:
    data.append(i*10)
imax=len(data)
i=0
while i<imax:
    data[i]+=data3[i]
    i+=1
file.write(bytes(data))