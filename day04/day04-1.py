# 48680
#
# https://adventofcode.com/2018/day/4
# find the guard that slept the most
# find the minute the guard was most often asleep
# multiply the minute times the guard number

import sys
import re
from collections import Counter
import pprint

# read in the file and sort by time
with open(sys.argv[1], 'r') as inputFile:
    ordered = [s.strip() for s in sorted(list(inputFile))]

#['[1518-11-05', '00', '03', 'Guard', '99', 'begins', 'shift']
#['[1518-11-05', '00', '45', 'falls', 'asleep']
#['[1518-11-05', '00', '55', 'wakes', 'up']
minutesAsleep = {}  # contains list of minutes asleep for each guard

# split on multiple chars
r = re.compile('[:\]# ]+')

guard = 0
sleep = 0
for line in ordered:
    tokens = r.split(line)
    if '#' in line:
        # change of guard
        guard = int(tokens[4])
        if guard in minutesAsleep.keys():
            pass
        else:
            minutesAsleep[guard] = []
    elif 'falls' in line:
        sleep = int(tokens[2])
    elif 'wakes' in line:
        wake = int(tokens[2])
        for m in range(sleep, wake):
            minutesAsleep[guard].append(m)
    else:
        print "error"

# the guard with the most minutes asleep has the longest minutesAsleep array
maxSleep = 0
maxSleeper = 0
for guard, minutes in minutesAsleep.items():
    totalAsleep = len(minutes)
    if totalAsleep > maxSleep:
        maxSleep = totalAsleep
        maxSleeper = guard


# now find minute most often asleep
minuteTotals = Counter(minutesAsleep[maxSleeper])
maxMinute = minuteTotals.most_common(1)[0][0]

print maxSleeper * maxMinute
