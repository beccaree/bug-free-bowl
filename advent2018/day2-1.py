import sys

doubles = 0
triples = 0

sys.stdin = open('input.txt', 'r')
for line in sys.stdin:
	charList = list(line)
	two = False
	three = False
	for char in charList:
		occurances = charList.count(char)
		if occurances == 2:
			two = True
		elif occurances == 3:
			three = True
	if two:
		doubles += 1
	if three:
		triples += 1

checksum = doubles * triples

print(checksum)

print("done")
