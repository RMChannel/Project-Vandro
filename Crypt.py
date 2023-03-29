from PIL import Image
import numpy as np
import os
path='1980089.jpeg'
extension=os.path.splitext(path)
extension=extension[1]
file=open(path,'rb')
datab=[]
datac=[]
data=list(file.read())
for i in data:
    b=i//10
    c=i%10
    datab.append(b)
    datac.append(c)
extension=list(extension.encode())
extension.append(len(extension))
datab+=extension
datac+=extension
a=len(datab)-1
while a>0:
    if len(datab)%a==0:
        print(a)
    a-=1
print(a)
datab=np.array_split(datab, 2)
print(datab)
arrayb = np.array(datab, dtype=np.int32)
arrayc = np.array(datac, dtype=np.int32)
imgb=Image.fromarray(arrayb)
imgc=Image.fromarray(arrayc)
imgb.save('b.png')
imgc.save('c.png')