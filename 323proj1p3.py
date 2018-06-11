data = open("data.txt")
with data as f:
    arr = f.readlines()
data.close()
arr = [x.strip() for x in arr] 

newarr = []
fullarr = []

def tokener(string):
	token = ["=" , "*" , "-" , ";" , "(" , ")" , "<=" ,"+", ","]
	inp = string
	for i in token:
		if i==";":
			inp = inp.replace(i, " "+i+"\n")
		else:
			inp = inp.replace(i, " "+i+" ")
	inp = inp.split(" ")

	newstring = ""
	for i in inp:
		if i!="":
			newstring+=i+" "

	if len(newstring)>0 and newstring[0]==" ":
		return newstring[2:]
	else:
		return newstring

def comment_cleaner(string):
	if string.find("//")!=-1:
		return string[0:string.index("//")]
	else:
		if string[0]==" ":
			return string.pop(0)
		else:
			return string
	
for i in arr:
	newarr.append(tokener(i))

for i in newarr:
	if i!="":
		if comment_cleaner(i)!="":
			fullarr.append(comment_cleaner(i))

newfile = open('newdata.txt', 'w')

for i in fullarr:
	if i[-1]==" ":
		newfile.write(i[0:-1])
	else:
		newfile.write(i)
newfile.close()