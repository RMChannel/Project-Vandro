from PIL import Image
import numpy as np
import os

def decrypt(pathb,pathc):
    file=open('decrypt','wb')
    file2=Image.open(pathb,'r')
    file3=Image.open(pathc,'r')
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

def crypt(path):
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
    arrayb = np.array(datab, dtype=np.int32)
    arrayc = np.array(datac, dtype=np.int32)
    imgb=Image.fromarray(arrayb)
    imgc=Image.fromarray(arrayc)
    imgb.save('b.png')
    imgc.save('c.png')