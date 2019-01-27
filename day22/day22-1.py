# 11575
#
# https://adventofcode.com/2018/day/22

import numpy as np 


# real
depth = 11541
target = (14,778) # x,y
target = (778, 14) # y, x

# test
#depth = 510
#target = (10,10)
# answer is 114

types = np.zeros((target[0]+ 1, target[1] + 1), dtype = int)
erosions = np.zeros((target[0]+ 1, target[1] + 1), dtype = int)
indexes = types = np.zeros((target[0]+ 1, target[1] + 1), dtype = int)

rocky = 0
narrow = 2
wet = 1

# rocky as ., wet as =, narrow as |
legend = {
    rocky : '.',
    wet : '=',
    narrow: '|'
}

#0 for rocky regions, 1 for wet regions, and 2 for narrow regions.

def printTypes():
    for row in types:
        print ''.join([legend[x] for x in row])

def getGeoIndex(y, x):


    if (y, x) == (0 , 0):
        #The region at 0,0 (the mouth of the cave) has a geologic index of 0.
        return 0
    elif (y, x) == target:
        #The region at the coordinates of the target has a geologic index of 0.
        return 0
    elif y == 0:
        #If the region's Y coordinate is 0, the geologic index is its X coordinate times 16807.
        return 16807 * x
    elif x == 0:
        #If the region's X coordinate is 0, the geologic index is its Y coordinate times 48271.
        return 48271 * y
    else:
        #Otherwise, the region's geologic index is the result of multiplying the erosion levels of the regions at X-1,Y and X,Y-1.
        return erosions[y, x-1] * erosions[y-1, x]

def getErosionLevel(y, x):
    # A region's erosion level is its geologic index plus the cave system's depth, all modulo 20183. 
    return (getGeoIndex(y, x) + depth) % 20183

def getType(erosionLevel):
    #If the erosion level modulo 3 is 0, the region's type is rocky.
    #If the erosion level modulo 3 is 1, the region's type is wet.
    #If the erosion level modulo 3 is 2, the region's type is narrow.
    if erosionLevel % 3 == 0:
        return rocky
    elif erosionLevel % 3 == 1:
        return wet
    else:
        return narrow

for y in range(0, target[0] + 1):
    for x in range(0, target[1] + 1):
        indexes[y,x] = getGeoIndex(y,x)
        erosions[y, x] = getErosionLevel(y, x)
        types[y,x] = getType(erosions[y,x])


#print grid
printTypes()
print np.sum(types)