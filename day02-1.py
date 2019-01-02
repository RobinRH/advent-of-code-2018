# 7134 
#
# https://adventofcode.com/2018/day/2

import sys
from collections import Counter

with open(sys.argv[1], 'r') as inputFile:
    lines = list(inputFile)


twos = 0
threes = 0
for line in lines:
    counts = Counter(line)
    if 2 in counts.values():
        twos += 1

    if 3 in counts.values():
        threes += 1

checksum = twos * threes
print checksum