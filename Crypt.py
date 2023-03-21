import math
import os
path='a.png'
extension=os.path.splitext(path)
extension=extension[1]
file=open(path,'rb')
file2=open('b','wb')
file3=open('c','wb')
datab=[]
datac=[]
data=list(file.read())
for i in data:
    b=i/10
    c=b-math.floor(b)
    c=int(round(c*10))
    b=math.floor(b)
    datab.append(b)
    datac.append(c)
extension=list(extension.encode())
datab.append(extension)
datac.append(extension)
file2.write(bytes(datab))
file3.write(bytes(datac))