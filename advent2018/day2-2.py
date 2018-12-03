import sys

doubles = 0
triples = 0
boxes = []

sys.stdin = open('input.txt', 'r')
for line in sys.stdin:
	charList = list(line)
	boxes.append(charList)

#assuming boxIds are all the same length
boxLength = len(boxes[0])

for i,box in enumerate(boxes):
	for otherBox in boxes[i+1:]:
		diff = 0
		for j, charX in enumerate(box):
			if charX != otherBox[j]:
				diff+=1
		if diff == 1:
			print(box)
			print(otherBox)
	
print("done")
