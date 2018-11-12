import sys
# For each row, determine the difference between the largest value and the smallest value; the checksum is the sum of all of these differences.

total = 0

for line in sys.stdin:
    values = line.split("\t")
    max = int(values[0])
    min = int(values[0])
    
    for num in values:
        number = int(num)
        if number > max:
            max = number
        if number < min:
            min = number
    
    diff = max - min
    total += diff
    
print(total)
