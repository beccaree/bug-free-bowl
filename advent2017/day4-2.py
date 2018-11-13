import sys

total = 0

for line in sys.stdin:
    values = line.split()
    valid = True
    
    for i, word in enumerate(values):
        x = list(word)
        x.sort()
        for otherWord in values[i+1:]:
            y = list(otherWord)
            y.sort()
            if x == y:
                valid = False
        
    if valid:
        total += 1
        
print(total)
