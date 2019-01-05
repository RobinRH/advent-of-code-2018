# FPRBRRZA, 10027
#
# https://adventofcode.com/2018/day/10

import sys
import numpy as np 
import pprint

def printStars(starsToPrint):
    # need to shift everything over to be postive
    minx = min([s[0] for s in starsToPrint])
    maxx = max([s[0] for s in starsToPrint])
    miny = min([s[1] for s in starsToPrint])
    maxy = max([s[1] for s in starsToPrint])

    ncols, nrows = (abs(maxy-miny) + 1, abs(maxx - minx) + 1)
    if max(nrows, ncols) > 300:
        return

    array = np.array(list(' ' * ncols * nrows), dtype = np.str).reshape((ncols, nrows))
    for s in starsToPrint:
        array[s[1] - miny, s[0] - minx] = '*' 

    for row in array:
        print ''.join(row)

if __name__ == "__main__": 

    with open(sys.argv[1], 'r') as inputFile:
        lines = [line.strip() for line in list(inputFile)]

    stars = []

    # position=<-3,  6> velocity=< 2, -1>
    # -3 6 2 -1
    # ['-3', '6', '2', '-1']
    for line in lines:
        line = line.replace('position=', '').replace('velocity=', '').replace('<', '').replace('>', '').replace(',', '').replace('  ', ' ').strip()
        tokens = line.split(' ')
        stars.append([int(s) for s in tokens])

    oldStars = stars
    for i in range(10027):
        newStars = [[xpos + xvel, ypos + yvel, xvel, yvel] for xpos, ypos, xvel, yvel in oldStars]
        oldStars = newStars

    printStars(oldStars)
    print i + 1
