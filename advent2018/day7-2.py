import sys
import math
import re

#Step F must be finished before step E can begin.
done = []
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
	if not letter in letterList:
		letterList.append(letter)

def workersNotDone(workers, time):
	if time == 0:
		return True
	for worker in workers:
		if len(worker) != 0:
			return True
	return False

seconds = 0
workers = [{} for i in range(5)]
while workersNotDone(workers, seconds):
	empty = []
	for i, worker in enumerate(workers):
		if len(worker) != 0:
			for letter in worker:
				worker[letter] -= 1
			if worker[letter] <= 0:
				done.append(letter)
				workers[i] = {}
				for c in dependencies:
					if letter in dependencies[c]:
						dependencies[c].remove(letter)
						if len(dependencies[c]) == 0:
							empty.append(c)
				for e in empty:
					dependencies.pop(e)
	noDependency = [x for x in letterList if not x in dependencies]
	noDependency.sort()
	for letter in noDependency:
		for emptyWorker in workers:
			if len(emptyWorker) == 0:
				emptyWorker[letter] = ord(letter) - 64 + 60 #ascii value of A
				letterList.remove(letter)
				break
	seconds += 1

print(seconds-1) # extra loop counted
print("done")
