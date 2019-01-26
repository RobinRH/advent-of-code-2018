# 120419
#
# https://adventofcode.com/2018/day/3

import sys
import numpy as np 
import re

with open(sys.argv[1], 'r') as inputFile:
    lines = [s.strip() for s in list(inputFile)]

fabric = np.zeros((1200, 1200))

# #1378 @ 648,606: 12x28
r = re.compile('[# @,:x]+')

for line in lines:
    claimId, x, y, width, height = [int(x) for x in r.split(line) if x]
    fabric[y:(y + height), x:(x + width)] += (np.zeros((height, width)) + 1)

answer = np.sum(fabric > 1)
print answer
