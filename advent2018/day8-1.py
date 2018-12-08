import sys
import math
import re

metadata = []

sys.stdin = open('input.txt', 'r')
for line in sys.stdin:
	tree = [int(x) for x in line.split(" ")]

totalMetadata = 0

def nodeLength(segment):
	global totalMetadata
	print(segment)
	numChild = int(segment[0])
	numMetadata = int(segment[1])
	result = 2 #first 2 data points is header
	if numChild == 0:
		for x in range(numMetadata):
			totalMetadata += segment[2+x]
		result += numMetadata
		return result
	else:
		children = segment[result:len(segment)-numMetadata]
		length = 0
		for i in range(numChild):
			l = nodeLength(children[length:])
			length += l
		for y in range(numMetadata):
			totalMetadata += segment[2+length+y]
		return result + length + numMetadata

nodeLength(tree)
print(totalMetadata)
print("done")
