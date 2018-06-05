
def parser(string):

	reservedwords = ["cout<<","for","int","while"]
	specialwords = ["<","=","*","-",";","(",")","<=","+",","]

	for token in string:
		found = False
		for reserved in reservedwords:
			if token.lower()==reserved:
				print token.lower(),"reserved word"
				found = True
		for special in specialwords:
			if token.lower()==special:
				print token.lower(),"special symbol"
				found = True
		if token.isdigit()==True:
			print token, "number"
			found = True
		if found == False:
			print token.lower(),"not identifier"

while True:
	input1 = raw_input("Enter a statement: ")
	parser(input1.split(" "))
	cont = raw_input("CONTINUE(y/n)?")
	if cont == "n":
		break
	elif cont == "y":
		pass
	else:
		pass