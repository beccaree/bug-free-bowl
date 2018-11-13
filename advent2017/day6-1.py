import sys

cycles = 0
pastPatterns = []

for line in sys.stdin:
    values = line.split("\t")
    numbers = list(map(int, values))
    pastPatterns.append(numbers[:])
    
found = False
while not found:
    cycles += 1
    maxI = 0
    
    for i, num in enumerate(numbers):
        if num > numbers[maxI]:
            maxI = i
    
    y = numbers[maxI]
    numbers[maxI] = 0
    while y > 0:
        maxI += 1
        if maxI == len(numbers):
            maxI = 0
        y -= 1
        numbers[maxI] += 1

    for pattern in pastPatterns:
        if numbers == pattern:
            found = True
    
    pastPatterns.append(numbers[:])

print(cycles)
