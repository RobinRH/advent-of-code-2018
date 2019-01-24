# 8638
#
# https://adventofcode.com/2018/day/20

import sys
import numpy as np 
from pprint import pprint

######## read lines in file
with open(sys.argv[1], 'r') as inputFile:
    lines = [s.strip().replace('^', '').replace('$','') for s in inputFile.readlines()]

rooms = []
rooms.append((0,0))
doors = []

maxdepth = 0
over1000 = 0

# ENWWW(NEEE|SSE(EE|N))
def runPath(regex, start, depth):
    global maxdepth
    global over1000
    srow, scol = start
    startDepth = depth
    if len(regex) == 0:
        return

    saves = []
    seen = []

    while True:
        if len(regex) == 0:
            saves.append(depth)
            maxsaves = max(saves)
            maxdepth = max(maxsaves, maxdepth)
            return depth
        nextMove = regex.pop(0)
        if nextMove == '(':
            saves.append(depth)
            depth = runPath(regex, (srow, scol), depth)
        elif nextMove == ')':
            saves.append(depth)
            maxsaves = max(saves)
            maxdepth = max(maxsaves, maxdepth)
            return depth
        elif nextMove == '|':
            #runPath(regex, (start[0], start[1]))
            saves.append(depth)
            srow, scol = start
            depth = startDepth
            seen = []
            #return
        else:
            if nextMove == 'N':
                newRoom = (srow-1, scol)
                if not newRoom in rooms and depth + 1 >= 1000:
                    over1000 += 1
                if seen and seen[-1] == 'S':
                    seen.pop()
                else:
                    depth += 1
                    seen.append('N')
            elif nextMove == 'E':
                newRoom = (srow, scol+1)
                if not newRoom in rooms and depth + 1 >= 1000:
                    over1000 += 1
                if seen and seen[-1] == 'W':
                    seen.pop()
                else:
                    depth += 1
                    seen.append('E')
            elif nextMove == 'S':
                newRoom = (srow+1, scol)
                if not newRoom in rooms and depth + 1 >= 1000:
                    over1000 += 1
                if seen and seen[-1] == 'N':
                    seen.pop()
                else:
                    depth += 1
                    seen.append('S')
            else: # nextMove = 'W':
                newRoom = (srow, scol-1)
                if not newRoom in rooms and depth + 1 >= 1000:
                    over1000 += 1
                if seen and seen[-1] == 'E':
                    seen.pop()
                else:
                    depth += 1
                    seen.append('W')

            newDoors = [((srow, scol), newRoom), (newRoom, (srow, scol))]
            rooms.append(newRoom)
            doors.extend(newDoors)
            srow, scol = newRoom

    saves.append(depth)
    maxsaves = max(saves)
    maxdepth = max(maxsaves, maxdepth)
    print 'here', maxdepth
    return max(saves)


def printRooms(rooms, doors):
    # make a grid big enough for the rooms and the doors
    # find row min and max
    rowmin = 10000
    rowmax = -10000
    colmin = 10000
    colmax = -100000
    for row, col in rooms:
        rowmin = min(row, rowmin)
        rowmax = max(row, rowmax)
        colmin = min(col, colmin)
        colmax = max(col, colmax)

    width = (colmax - colmin + 1) * 2 + 1
    height = (rowmax - rowmin + 1) * 2 + 1
    size = width * height
    facility = np.array(list('#' * size), dtype=np.dtype(str))
    facility = np.reshape(facility, (height, width))
    #print facility

    #print 'here'
    for row, col in rooms:
        newRow = (row - rowmin) * 2 + 1
        newCol = (col - colmin) * 2 + 1
        #print (row, col), '->', (newRow, newCol)
        facility[newRow, newCol] = '.'

    ctr = 1
    for a, b in doors:
        arow, acol = a
        brow, bcol = b

        arow -= rowmin
        acol -= colmin
        brow -= rowmin
        bcol -= colmin

        # figure out the top, left of the two doors
        #print a, b
        if arow == brow: # left-right door
            if acol < bcol:
                facility[arow * 2 + 1, acol*2 + 2] = '|'
            else:
                facility[arow * 2 + 1, bcol*2 + 2] = '|'
        else: # up-down door
            if arow < brow:
                facility[arow * 2 + 2, acol*2 + 1] = '-'
            else:
                facility[brow * 2 + 2, acol*2 + 1] = '-'
        ctr += 1

    # add the origin
    facility[(0-rowmin)*2 + 1, (0-colmin)*2 + 1] = 'X'

    #np.array(list(data), dtype=np.dtype(str))
    for row in facility:
        print ''.join(row)
    print
    return rowmin, rowmax, colmin, colmax


# find the shortest path to each room
# which has the most doors?


# ENWWW(NEEE|SSE(EE|N))
for regex in lines:

    if regex.startswith('#'):
        continue

    rooms = []
    rooms.append((0,0))
    doors = []
    depth = 0
    maxdepth = 0
    over1000 = 0
    depth = runPath(list(regex), (0,0), 0)
    print 'maxdepth:', maxdepth, 'over 1000:', over1000
    print
    continue




