import fileinput
import os

f=open("glist.txt","r")
for x in f:
	x=x.rstrip("\n")
	name=x+'.txt'
	print(name)
	filename = open(name,"a+")
	with fileinput.FileInput("Message-Dummy.txt", inplace=True) as file:
		for line in file:
			print(line.replace("X",x), end='')
	filename2 = open("Message-Dummy.txt","r+")
	for a in filename2:
		filename.write(a)
	os.remove("Message-Dummy.txt")
	filename2 = open("Message-Dummy.txt","a+")
	filename3 =open("Message.txt","r+")
	for l in filename3:
		filename2.write(l)
	filename.close()
	filename2.close()
	filename3.close()
f.close()