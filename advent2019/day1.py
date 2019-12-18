import sys

totalFuel = 0

def recurseFuel(mass):
	fuel = mass // 3 - 2
	if fuel > 0:
		return fuel + recurseFuel(fuel)
	else:
		return 0

sys.stdin = open('input.txt', 'r')
for line in sys.stdin:
	mass = int(line)
	# fuel = mass // 3 - 2
	# totalFuel += fuel
	totalFuel += recurseFuel(mass)

print(totalFuel)

print("done")
