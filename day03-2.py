# 445
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

claims = []
for line in lines:
    claimId, x, y, width, height = [int(x) for x in r.split(line) if x]
    claims.append((claimId, x, y, width, height))

for (claimId, x, y, width, height) in claims:
    fabric[y:(y + height), x:(x + width)] += (np.zeros((height, width)) + 1)

for (claimId, x, y, width, height) in claims:
    # expect sum to equal size, because all values are 1
    size = height * width
    if np.sum(fabric[y:(y + height), x:(x + width)]) == size:
        print claimId
        break
