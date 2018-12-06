import sys
import math

points = []

maxX = 0
maxY = 0

sys.stdin = open('input.txt', 'r')
for line in sys.stdin:
	line = line.strip()
	point = line.split(",")
	point[0] = int(point[0])
	point[1] = int(point[1])
	points.append(point)
	if (point[0] > maxX):
		maxX = point[0]
	if (point[1] > maxY):
		maxY = point[1]

numPoints = len(points)
grid = [[0 for ix in range(maxX + 2)] for iy in range(maxY + 2)]
areaForPoint = {}

print(grid)

for x in range(maxX):
	for y in range(maxY):
		minDist = maxX + maxY
		bestPoint = -1
		for i, point in enumerate(points):
			dist = abs(x - point[0]) + abs(y - point[1])
			if dist < minDist:
				minDist = dist
				bestPoint = i
			elif dist == minDist:
				bestPoint = -1
		
		grid[x][y] = bestPoint
		if bestPoint in areaForPoint:
			areaForPoint[bestPoint] += 1
		else:
			areaForPoint[bestPoint] = 1

maxArea = 0
for point in areaForPoint:
	area = areaForPoint[point]
	if area > maxArea:
		maxArea = area

print(maxArea)
print("done")
