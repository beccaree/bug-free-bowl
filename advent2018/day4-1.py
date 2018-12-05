import sys
import re

logs = []

sys.stdin = open('input.txt', 'r')
# [1518-11-01 00:05] falls asleep
for line in sys.stdin:
	m = re.search('\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\]', line)
	log = {
		"year": int(m.group(1))
		"month": int(m.group(2))
		"day": int(m.group(3))
		"hour": int(m.group(4))
		"minute": int(m.group(5))
		"activity": line[(line.find(']')+2):] #including space
	}


print("done")	

#year = int(m.group(1))
#day = int(m.group(3))
#hour = int(m.group(4))
#month = int(m.group(2))
#minute = int(m.group(5))
#activity = line[(line.find(']')+2):] #including space
