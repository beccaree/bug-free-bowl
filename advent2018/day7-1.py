import sys
import math
import re

#Step F must be finished before step E can begin.
finalOrder = ''
dependencies = {}
letterList = []

sys.stdin = open('input.txt', 'r')
for line in sys.stdin:
	m = re.search('Step (\w) must be finished before step (\w) can begin', line)
	dependsOn = m.group(1)
	letter = m.group(2)
	if letter in dependencies:
		dependencies[letter].append(dependsOn)
	else:
		dependencies[letter] = [dependsOn]

	if not dependsOn in letterList:
		letterList.append(dependsOn)

# while letterlist not empty
while len(letterList) > 0:
	noDependency = [x for x in letterList if not x in dependencies]
	noDependency.sort()
	empty = []
	letter = noDependency[0]
	finalOrder += letter
	letterList.remove(letter)
	for c in dependencies:
		if letter in dependencies[c]:
			dependencies[c].remove(letter)
			if len(dependencies[c]) == 0:
				empty.append(c)
	for e in empty:
		dependencies.pop(e)
		
print(finalOrder + e)
print("done")
