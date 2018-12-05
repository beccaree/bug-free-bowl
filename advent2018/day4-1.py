import sys
import re
import operator

logs = []
guardId = 0
minuteAsleep = 0

sys.stdin = open('input.txt', 'r')
# [1518-11-01 00:05] falls asleep
for line in sys.stdin:
	#line = '[1518-11-01 00:05] falls asleep'
	m = re.search('\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\]', line)
	hour = int(m.group(4))
	if hour == 0: #mignight
		hour = 24
	log = {
		"year": int(m.group(1)),
		"month": int(m.group(2)),
		"day": int(m.group(3)),
		"hour": hour,
		"minute": int(m.group(5)),
		"detail": line[(line.find(']')+2):] #including space
	}
	logs.append(log)
	
# sort the logs by date time
logs.sort(key = operator.itemgetter("day", "hour", "minute"))

print(logs)

# split logs into guard specific and record sleep time
# array of minutes per guard

print("done")	

#year = int(m.group(1))
#day = int(m.group(3))
#hour = int(m.group(4))
#month = int(m.group(2))
#minute = int(m.group(5))
#detail = line[(line.find(']')+2):] #including space
