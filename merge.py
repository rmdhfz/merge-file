import shutil

print("\nUsing the shutil.copyfileobj() method")

fristfile 	= input("\nName of the first file 		:	")
secondfile 	= input("\nName of the second file 	:	")
newfile 	= input("\nName of the new file 		:	")

with open(newfile, 'w') as newfiles:
	for i in [fristfile, secondfile]:
		with open(i, 'r') as f1:
			newfiles.write(f1.read())
			newfiles.write("\n\n")

print("\nFiles merged successfully into : ", newfile)
print("\nContents of new file : \n")
with open(newfile, 'r') as n:
	print(n.read())