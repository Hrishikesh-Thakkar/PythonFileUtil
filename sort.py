import os
FileName = ("guestlist.txt")
data=open(FileName,"r").readlines()
data.sort()
f = open("glist.txt","a+")
for i in range(len(data)):
    f.write(data[i])