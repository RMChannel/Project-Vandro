from PIL import Image
import numpy as np
import os
def findprimenumbers(n):
    listnumber=[]
    i=2
    while i<n:
        if n%i==0:
            listnumber.append(i)
            n/=i
            i=2
        else: i+=1
        if i==n:
            listnumber.append(i)
    if len(listnumber)%2==0: middle=int((len(listnumber))/2)
    else: middle=int((len(listnumber)-1)/2)
    i=0
    n=1
    while i<middle:
        n=n*listnumber[i]
        i+=1
    return n

path='a.png'
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
lenn=findprimenumbers(len(datab))
datab=np.matrix(np.array_split(datab,lenn))
datac=np.matrix(np.array_split(datac,lenn))
imgb=Image.fromarray(datab)
imgc=Image.fromarray(datac)
imgb.save('b.png')
imgc.save('c.png')