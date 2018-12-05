import sys
import math

sys.stdin = open('input.txt', 'r')
for line in sys.stdin:
	polymer = list(line)

def reactPolymer(polymer):
	while True:
		reaction = False
		for i, char in enumerate(polymer[1:]):
			front = ord(polymer[i])
			back = ord(char)
			diff = front - back
			if math.fabs(diff) == 32: #diff between captial and non capital of letter
				polymer = polymer[:i] + polymer[i+2:]
				reaction = True
				break
		if not reaction:
			break
	return(len(polymer))

minX = len(polymer)
for n in range(26):
	testPolymer = polymer.copy()
	uppercase = chr(65 + n)
	lowercase = chr(65 + 32 + n)
	testPolymer = [x for x in testPolymer if x != uppercase and x != lowercase]
	
	length = reactPolymer(testPolymer)
	if length < minX:
		minX = length
	print(n)

print(reactPolymer(polymer))
print(minX)
print("done")
