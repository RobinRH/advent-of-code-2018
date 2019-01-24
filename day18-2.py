# 189168
#
# https://adventofcode.com/2018/day/4

import sys
import numpy as np 
import re
from collections import Counter
import pprint

######## read lines in file
with open(sys.argv[1], 'r') as inputFile:
    lines = map(lambda s: s.strip(), list(inputFile))

rows = len(lines)
cols = len(lines[0])
data = ''.join(lines)

landscape = np.array(list(data), dtype=np.dtype(str))
landscape = np.reshape(landscape, (rows, cols))

landscape = np.pad(landscape, 1, 'constant')

def printLandscape(landscape):
    for row in landscape:
        print ''.join(row)

def changeLandscape(landscape):
    newLandscape = np.copy(landscape)
    #An open acre will become filled with trees if three or more adjacent acres contained trees. Otherwise, nothing happens.
    neighbors = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1)
    ]

    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            #An open acre will become filled with trees if three or more adjacent acres contained trees.
            # Otherwise, nothing happens.
            trees = 0
            for rowdiff, coldiff in neighbors:
                if landscape[r + rowdiff, c + coldiff] == '|':
                    trees += 1
            if trees >= 3 and landscape[r, c] == '.':
                #print r, c, 'new tree'
                newLandscape[r, c] = '|'
             
            #An acre filled with trees will become a lumberyard if three or more adjacent acres were lumberyards.
            # otherwise, nothing
            yards = 0
            for rowdiff, coldiff in neighbors:
                if landscape[r + rowdiff, c + coldiff] == '#':
                    yards += 1
            if yards >= 3 and landscape[r, c] == '|':
                newLandscape[r, c] = '#'

            #An acre containing a lumberyard will remain a lumberyard if it was adjacent to at least one other lumberyard 
            # and at least one acre containing trees. Otherwise, it becomes open.
            if landscape[r, c] == '#':
                if yards >= 1 and trees >= 1:
                    pass
                else:
                    #print r, c, 'losing a yard', 'yards', yards, 'trees', trees
                    newLandscape[r, c] = '.'

    return newLandscape

def landscapeToString(landscape):
    return ''.join(landscape.flatten())


results = []
landscape479 = None
first = None
second = None
for i in range(600):
    landscape = changeLandscape(landscape)
    s = landscapeToString(landscape)
    
    if s in results:
        first = results.index(s)
        second = i
        landscape479 = landscape
        break #pass
    else:
        results.append(s)

more = (1000000000 - 1 - first) % (second - first)

landscape = landscape479
for m in range(more):
    landscape = changeLandscape(landscape)

woods = (landscape == '|')
yards = (landscape == '#')
print np.sum(woods) * np.sum(yards)


