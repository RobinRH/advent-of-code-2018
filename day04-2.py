# 94826
#
# https://adventofcode.com/2018/day/4

import sys
import re
from collections import Counter
import pprint

with open(sys.argv[1], 'r') as inputFile:
    ordered = [s.strip() for s in sorted(list(inputFile))]

#['[1518-11-05', '00', '03', 'Guard', '99', 'begins', 'shift']
#['[1518-11-05', '00', '45', 'falls', 'asleep']
#['[1518-11-05', '00', '55', 'wakes', 'up']
minutesAsleep = {}  # contains list of minutes asleep

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

# across all guards, find the minute most often asleep by which guard
maxTimes = 0
maxMinute = 0
maxGuard = 0
for guard, minutes in minutesAsleep.items():
    agg = Counter(minutes)
    for key, value in agg.items():
        if value > maxTimes:
            maxMinute = key
            maxTimes = value
            maxGuard = guard

print maxGuard * maxMinute
