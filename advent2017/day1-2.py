"""
- 1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
- 1221 produces 0, because every comparison is between a 1 and a 2.
- 123425 produces 4, because both 2s match each other, but no other digit has a match.
- 123123 produces 12.
- 12131415 produces 4.
"""

s = input("Input: ")
numbers = list(s)
length = len(numbers)
shift = length/2
total = 0

for i, num in enumerate(numbers):
  nextIndex = int((i + shift) % length)
  
  if num == numbers[nextIndex]:
    total += int(num)

print("Result: ", total)
