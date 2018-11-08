"""
- 1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2) matches the fourth digit.
- 1111 produces 4 because each digit (all 1) matches the next.
- 1234 produces 0 because no digit matches the next.
- 91212129 produces 9 because the only digit that matches the next one is the last digit, 9.
"""

s = input("Input: ")
numbers = list(s)
length = len(numbers)
total = 0

for i, num in enumerate(numbers):
  nextIndex = i + 1
  if i + 1 == length:
    nextIndex = 0
  
  if num == numbers[nextIndex]:
    total += int(num)

print("Result: ", total)
