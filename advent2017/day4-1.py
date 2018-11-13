import sys

total = 0

for line in sys.stdin:
    values = line.split()
    valid = True
    
    for i, word in enumerate(values):
        for otherWord in values[i+1:]:
            if word == otherWord:
                valid = False
        
    if valid:
        total += 1
        
print(total)
