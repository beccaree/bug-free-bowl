import sys

steps = 0
instructions = []

for line in sys.stdin:
    instructions.append(int(line))

i = 0    
while True:
    steps += 1
    x = instructions[i]
    instructions[i] += 1
    
    i += x
    if i < 0 or i >= len(instructions):
        break

print(steps)
