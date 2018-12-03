import sys

frequency = 0
changeList = []
pastFreq = [0]

sys.stdin = open('input.txt', 'r')
for line in sys.stdin:
	change = int(line)
	changeList.append(change)

foundDup = False
print(changeList)
listLen = len(changeList)
i = 0
while not foundDup:
	frequency += changeList[i]
	if frequency in pastFreq:
		print(frequency)
		foundDup = True
	else:
		pastFreq.append(frequency)
		i+=1
		if i == listLen:
			i=0

print("done")
