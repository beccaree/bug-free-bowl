import sys
import re
import operator

logs = []
guardId = 0
mostAsleep = 0

sys.stdin = open('input.txt', 'r')
# [1518-11-01 00:05] falls asleep
for line in sys.stdin:
	m = re.search('\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\]', line)
	log = {
		"year": int(m.group(1)),
		"month": int(m.group(2)),
		"day": int(m.group(3)),
		"hour": int(m.group(4)),
		"minute": int(m.group(5)),
		"detail": line[(line.find(']')+2):len(line)-1] #including space, not including new line char
	}
	logs.append(log)
	
# sort the logs by date time
logs.sort(key = operator.itemgetter("month", "day", "hour", "minute"))

# split logs into guard specific and record sleep time
sleepSchedule = {}
currentGuardId = 0
fellAsleep = 0
for log in logs:
	# check if a new guy started shift
	digits = re.findall(r'\d+', log["detail"])
	if len(digits) > 0:
		currentGuardId = digits[0]
	elif log["detail"] == "falls asleep":
		fellAsleep = log["minute"]
	elif log["detail"] == "wakes up":
		key = str(currentGuardId)
		slept = log["minute"] - fellAsleep
		if not key in sleepSchedule:
			# make new entry
			sleepSchedule[key] = [0] * 59
		for i in range(slept):
			sleepSchedule[key][fellAsleep + i] += 1

# count sum of all minutes in each schedule
maxKey = 0
max = 0
for scheduleKey in sleepSchedule:
	sum = 0
	for n in sleepSchedule[scheduleKey]:
		sum += n
	if sum > max:
		max = sum
		maxKey = scheduleKey

guardId = int(maxKey)

# for max schedule, find max number and get index
schedule = sleepSchedule[maxKey]
for i, n in enumerate(schedule):
	if n > schedule[mostAsleep]:
		mostAsleep = i

print(guardId * mostAsleep)

print("done")
