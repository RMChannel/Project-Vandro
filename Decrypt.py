from PIL import Image
import numpy as np
import os
file=open('decrypt','wb')
file2=Image.open('b.png','r')
file3=Image.open('c.png','r')
data2=list(file2.getdata())
data3=list(file3.getdata())
i=1
extension=[]
len2=data2[-1]
while i<=len2:
    extension.append(data2[-i-1])
    i+=1
i=0
while i<=len2:
    data2.pop(-1)
    data3.pop(-1)
    i+=1
extension=bytes(extension).decode()
extension=extension[::-1]
print(extension)
data=[]
i=0
for i in data2:
    data.append(i*10)
imax=len(data)
i=0
while i<imax:
    data[i]+=data3[i]
    i+=1
file.write(bytes(data))
file.close()
file2.close()
file3.close()
os.rename("decrypt","decrypt"+extension)