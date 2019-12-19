import sys

sys.stdin = open('input.txt', 'r')
line = sys.stdin.readline()
arr = line.split(',')

nums = [int(x) for x in arr]
clone = []

def checkPair(noun, verb):
	clone = list(nums)
	clone[1] = noun
	clone[2] = verb
	for i in range(0, len(clone), 4):
		x = clone[i]
		if x == 99: # end program
			break

		x1 = clone[i+1]
		x2 = clone[i+2]
		result = clone[i+3]

		if x == 1: # addition
			clone[result] = clone[x1] + clone[x2]

		if x == 2: # multiplication
			clone[result] = clone[x1] * clone[x2]

	if clone[0] == 19690720:
		print(100 * noun + verb)
		return True
	else:
		clone = []
		return False

for o in range(0, 99):
	for w in range(0, 99):
		if checkPair(o, w):
			break

print("done")
