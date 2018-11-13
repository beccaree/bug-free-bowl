import sys

steps = 0
instructions = []

for line in sys.stdin:
    instructions.append(int(line))

i = 0
while True:
    steps += 1
    x = instructions[i]
    
    if x < 3: 
        instructions[i] += 1
    else:
        instructions[i] -= 1
    
    i += x
    if i < 0 or i >= len(instructions):
        break

print(steps)
