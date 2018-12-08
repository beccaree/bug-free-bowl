import sys
import math
import re

metadata = []

sys.stdin = open('input.txt', 'r')
for line in sys.stdin:
	tree = [int(x) for x in line.split(" ")]

totalMetadata = 0
totalValue = 0

def nodeLength(segment):
	global totalMetadata
	global totalValue
	numChild = int(segment[0])
	numMetadata = int(segment[1])
	result = 2 #first 2 data points is header
	if numChild == 0:
		v = 0
		for x in range(numMetadata):
			totalMetadata += segment[2+x]
			v += segment[2+x]
		result += numMetadata
		return [result, v]
	else:
		children = segment[result:len(segment)-numMetadata]
		length = 0
		childValues = []
		v = 0
		for i in range(numChild):
			f = nodeLength(children[length:])
			l = f[0]
			childValues.append(f[1])
			length += l
		for y in range(numMetadata):
			totalMetadata += segment[2+length+y]
			a = segment[2+length+y]
			if a <= numChild:
				v += childValues[a-1]
		return [result + length + numMetadata, v]

result = nodeLength(tree)

print(totalMetadata)
print(result[1])
print("done")
