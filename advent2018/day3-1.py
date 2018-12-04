import sys
import re

fabric = [[0] * 1100 for i in range(1100)]
total = 0

def drawFabric(x, y, width, height):
	for ix in range(width):
		for iy in range(height):
			fabric[x+ix][y+iy] += 1

# example input #1 @ 37,526: 17x23
sys.stdin = open('input.txt', 'r')
for line in sys.stdin:
	m = re.search('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line)	
	id = int(m.group(1))
	x = int(m.group(2))
	y = int(m.group(3))
	width = int(m.group(4))
	height = int(m.group(5))
	
	drawFabric(x, y, width, height)
	
for row in fabric:
	for squareInch in row:
		if squareInch > 1:
			total+=1

print(total)
print("done")
