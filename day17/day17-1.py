# part1: 30737
# part2: 24699
# https://adventofcode.com/2018/day/17



import sys
import numpy as np 
import re
from collections import Counter
from pprint import pprint

sys.setrecursionlimit(4000)

######## read lines in file
with open(sys.argv[1], 'r') as inputFile:
    lines = map(lambda s: s.strip(), list(inputFile))


'''
x=495, y=2..7
y=7, x=495..501
x=501, y=3..7
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504
'''
# the pattern (x or y)=num, (x or y)=num..num
lines = [s.replace('=', ' ').replace(',', '').replace('..', ' ') for s in lines]
readings = [s.split(' ') for s in lines]

def getMax(xory):
    xmax = 0
    for reading in readings:
        if reading[0] == xory:
            xmax = max(xmax, int(reading[1]))

        if reading[2] == xory:
            xmax = max(xmax, int(reading[4]))

    return xmax

def getMin(xory):
    xmin = 2500
    for reading in readings:
        if reading[0] == xory:
            xmin = min(xmin, int(reading[1]))

        if reading[2] == xory:
            xmin = min(xmin, int(reading[3]))

    return xmin


xmin = getMin('x')
xmax = getMax('x')
ymin = getMin('y')
ymax = getMax('y')

grid = np.zeros((ymax+ 1, xmax + 2), dtype=np.int8)


sand = 0
clay = 1
water = 2
well = 3
visited = 4
errNum = 5

legend = {
    0: '.',
    1: '#',
    2: '~',
    3: '+',
    4: '|',
    5: 'e'
}
for reading in readings:
    # y=13, x=498..504

    if reading[0] == 'x':
        x = int(reading[1])
        for y in range(int(reading[3]), int(reading[4]) + 1):
            grid[y, x] = clay

    if reading[0] == 'y':
        y = int(reading[1])
        for x in range(int(reading[3]), int(reading[4]) + 1):
            grid[y, x] = clay

grid[0, 500] = well
grid[:,0:1] = clay
grid[:,-1] = clay

def printGrid():
    smallGrid = grid[ymin:ymax+1, xmin:xmax+2]

    for row in smallGrid:
        charLine = [legend[s] for s in row]
        print ''.join(charLine)
    print

def dropWater(dropRow, dropCol):
    # go down until you hit something

    while dropRow + 1 <= ymax and grid[dropRow + 1, dropCol] in [sand, visited]:
        grid[dropRow, dropCol] = visited
        dropRow += 1
        if dropRow == ymax:
            grid[dropRow, dropCol] = visited
            return

    # if bounded on both sides with clay, fill in
    leftBounded = False
    leftDrop = False, -1
    left = dropCol
    while left -1 >= xmin:
        if grid[dropRow+1, left -1] in [sand, visited]: # it could drop
            leftDrop = True, left - 1
            break

        if grid[dropRow, left - 1] == clay:
            leftBounded = True
            break
        left -= 1

    rightBounded = False
    rightDrop = False, -1
    right = dropCol
    while right + 1 <= xmax:
        if grid[dropRow+1, right + 1] in [sand, visited]: # it could drop
            rightDrop = True, right + 1
            break

        if grid[dropRow, right + 1] == clay:
            rightBounded = True
            break
        right += 1

    #print dropRow, leftBounded, rightBounded, left, right



    #ld rd lb rb True True True True
    #ld rd lb rb True False True True
    #ld rd lb rb False True True True
    #ld rd lb rb False False True True
    if leftBounded and rightBounded:
        for col in range(left, right+1):
            grid[dropRow, col] = water
        # see if there are any drops in between the left and right bound # new code
        for col in range(left, right + 1):
            if grid[dropRow+1, col] in [sand, visited]:
                dropWater(dropRow + 1, col)
    #ld rd lb rb True True True False
    #ld rd lb rb True True False True
    #ld rd lb rb True True False False
    elif leftDrop[0] and rightDrop[0]:
        for col in range(leftDrop[1], rightDrop[1] + 1):
            grid[dropRow, col] = visited            
        dropWater(dropRow, leftDrop[1])
        dropWater(dropRow, rightDrop[1])
    #ld rd lb rb False True True False
    elif leftBounded and rightDrop[0]:
        for col in range(left, rightDrop[1]+1):
            grid[dropRow, col] = visited
        dropWater(dropRow, rightDrop[1])
    #ld rd lb rb True False False True
    elif rightBounded and leftDrop[0]:
        for col in range(leftDrop[1], right+1):  #for col in range(dropCol, right + 1):
            grid[dropRow, col] = visited
        dropWater(dropRow, leftDrop[1])
    #ld rd lb rb True False False False
    elif leftDrop[0] and not rightDrop[0] and not leftBounded and not rightBounded:
        grid[dropRow, leftDrop[1]] = errNum
        # this occurs near the bottom right
        for col in range(leftDrop[1], xmax+1):
            #print 'wrote at ', dropRow, col
            grid[dropRow, col] = visited
            dropWater(dropRow, leftDrop[1])
    #ld rd lb rb True False True False
    #ld rd lb rb False False True False
    #ld rd lb rb False True False False
    #ld rd lb rb False False False False
    #ld rd lb rb False True False True
    #ld rd lb rb False False False True
    else:
        print 'an error?', leftDrop, rightDrop, leftBounded, rightBounded
        # all leftDrop = (True, 565) rightDrop = (False, -1)leftBounded= False rightBounded = False

    #printGrid()
    return




def waterReach():
    # only count water and visited on the smaller grid.
    smallGrid = grid[ymin:ymax+1, xmin:xmax+2]


    nwater = np.sum(smallGrid == water)
    nvisited = np.sum(smallGrid == visited)
    nsand = np.sum(smallGrid == sand)
    nclay = np.sum(smallGrid == clay)
    #print nwater, nvisited, nsand, nclay, smallGrid.shape
    #print nwater, nvisited
    #return nwater + nvisited - 1 # -1 because I have one extra row at the top
    return nwater, nvisited

print "Takes a long time to run..."
same = False
drops = 0
while not same:
    oldwater, oldvisited = waterReach()
    dropWater(0, 500)
    newwater, newvisited = waterReach()
    same = (newwater == oldwater) and (newvisited == oldvisited)
    drops += 1
    if drops > 166:
        break

printGrid()
print 'drops', drops
nwater, newvisited = waterReach()
print nwater, newvisited
print 'part 1: ', nwater + newvisited + 12
print 'part 2: ', nwater

# add 12 for the far right side
