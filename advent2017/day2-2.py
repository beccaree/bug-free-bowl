import sys

total = 0

for line in sys.stdin:
    values = line.split("\t")
    numbers = list(map(int, values))
    numbers.sort(reverse=True)
    result = 0
    
    # order first
    for i, numerator in enumerate(numbers):
        for denominator in numbers[i+1:]:
            if (numerator % denominator) == 0:
                result = numerator/denominator
                break
            
    total += result
    
print(total)
