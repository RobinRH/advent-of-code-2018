# 713
#
# https://adventofcode.com/2018/day/23

import sys
import numpy as np 
import re
from collections import Counter
import pprint
from collections import namedtuple

######## read lines in file
with open(sys.argv[1], 'r') as inputFile:
    lines = map(lambda s: s.strip().replace('pos=<', '').replace(',', ' ').replace('>  r=', ' '), list(inputFile))

#pos=<0,0,0>, r=4
# x, y, z, radius

points = []
Point = namedtuple('Point', 'x y z radius')
maxRadius = 0
maxPoint = []
for line in lines:
    ints = line.split(' ')
    ints  = [int(x) for x in ints]
    points.append(ints)
    maxRadius = max(maxRadius, ints[3])
    if maxRadius == ints[3]:
        maxPoint = ints


# find all points within radius
count = 0
for point in points:
    if abs(point[0]-maxPoint[0]) + abs(point[1] - maxPoint[1]) + abs(point[2] - maxPoint[2]) <= maxRadius:
        count += 1

print count
