# 104501042
#
# https://adventofcode.com/2018/day/23

import sys
from collections import namedtuple

def distance(p1, p2):
    return abs(p1.x-p2.x) + abs(p1.y - p2.y) + abs(p1.z - p2.z)

# read lines in file
with open(sys.argv[1], 'r') as inputFile:
    lines = map(lambda s: s.strip().replace('pos=<', '').replace(',', ' ').replace('>  r=', ' '), list(inputFile))

# pos=<0,0,0>, r=4
# x, y, z, radius

# closest distance from origin to a bot is the
# manhattan distance minus the radius (work it out on graph paper)
# The shortest distance to all the bots is the largest
# of the manhattan distances.
Point = namedtuple('Point', 'x y z radius')
tokens  = [[int(x) for x in line.split(' ')] for line in lines]
points = [Point(*nano) for nano in tokens]
onepoint = Point(x=60247420, y=23331398, z=23302822, radius=0) # 82 106881640
winningset = [point for point in points if distance(point, onepoint) <= point.radius]
shortDistances = [(abs(star.x) + abs(star.y) + abs(star.z) - star.radius) for star in winningset]
print max(shortDistances)


