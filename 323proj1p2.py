input1 = raw_input("Input string and end with $:\n")


state = {0:{"a":0,"b":1},
			1:{"a":2,"b":1},
			2: {"a":2,"b":1}}
pos = 0
print "starting state", pos
for i in input1:
	if i=="$":
		break
	print "state",pos,"input",i, "transition to state",state[pos][i]
	pos = state[pos][i]

if pos ==2:
	print "YES"
else:
	print "NO"