import sys
import re
import operator

logs = []
sleepSchedule = []
guardId = 0
minuteAsleep = 0

sys.stdin = open('input.txt', 'r')
# [1518-11-01 00:05] falls asleep
for line in sys.stdin:
	#line = '[1518-11-01 00:05] falls asleep'
	m = re.search('\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\]', line)
	hour = int(m.group(4))
	if hour == 23: #mignight
		hour = -1
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

# split logs into guard specific and record sleep time
currentGuardId = 0
for log in logs:
	# check if a new guy started shift
		# set currentGuardId
	# else check if start
		# set start minute 
	# else check if end
		# get time difference
		# record in sleepSchedule for currentGuardId
		
# count all minutes in each schedule

# for max schedule, find max number and get index

print(guardId * minuteAsleep)

print("done")
