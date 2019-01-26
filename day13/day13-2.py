# 35,59 (col, row)
#
# https://adventofcode.com/2018/day/13

import sys
import numpy as np 
import re
from collections import Counter
import pprint

with open(sys.argv[1], 'r') as inputFile:
    lines = map(lambda s: s[0:-1], list(inputFile))

rows = len(lines)
cols = len(lines[0])
#print lines
track = np.array(list(' ' * rows * cols)).reshape((rows, cols))

def printTrack():
    printTrack = np.copy(track)
    for car in carsById.keys():
        row, col, direction, nextTurn, carId, crashed = carsById[car]
        if not crashed:
            printTrack[row, col] = direction

    for row in printTrack:
        print ''.join(row)

    print

#def deleteCarById(id):
#    carKey = 0
#    for car in carsById.keys():
#        row, col, direction, nextTurn, carId = carsById[car]
#        if carId == id:
#            carKey = car
#
#    del carsById[carKey]
#    #print 'deleted:', id, cars

carsById = {}
carCount = 0
for r in range(len(lines)):
    row = list(lines[r])
    for c in range(len(row)):
        track[r, c] = row[c]
        if row[c] == 'v':
            carsById[carCount] = (r, c, 'v', 'L', carCount, False)
            carCount += 1
            track[r, c] = '|'
        elif row[c] == '^':
            carsById[carCount] = (r, c, '^', 'L', carCount, False)
            carCount += 1
            track[r, c] = '|'
        elif row[c] == '>':
            carsById[carCount] = (r, c, '>', 'L', carCount, False)
            carCount += 1
            track[r, c] = '-'
        elif row[c] == '<':
            carsById[carCount] = (r, c, '<', 'L', carCount, False)
            carCount += 1
            track[r, c] = '-'


def getCarsSortedByLocation():
    # if two cars in the same place, that's a problem
    # this happens if a car passes through and accident location
    # make a dictionary of locations and keys
    locationsId = {}
    for row, col, direction, nextTurn, carId, crashed in carsById.values():
        if crashed:
            locationsId[0] = carId
        else:
            locationsId[row * 1000 + col] = carId

    idsByLocation = []
    for loc in list(sorted(locationsId.keys())):
        idsByLocation.append(locationsId[loc])

    return idsByLocation        

def isACrash(r, c):
    for carId in carsById.keys():
        row, col, direction, nextTurn, carId, crashed = carsById[carId]
        # if it's in the same location and not already crashed
        if (not crashed) and r == row and c == col:
            #print 'the other car is:', carId
            return True

    return False 

def crashTheCars(r, c):
    ids = []
    for carId in carsById.keys():
        row, col, direction, nextTurn, carId, crashed = carsById[carId]
        if row == r and col == c:
            if not crashed:
                carsById[carId] = (row, col, direction, nextTurn, carId, True)
                ids.append(carId)
                #print 'crashed:', carId

    return ids
    

def countCrashedCars(cars):
    total = 0
    for row, col, direction, nextTurn, carId, crashed in cars.values():
        if crashed:
            total += 1

    return total

#printTrack()

steps = 0
while True:

    carsByLoc = getCarsSortedByLocation()
    for carId in carsByLoc:
        #print 'no of cars', len(carsByLoc)
        row, col, direction, nextTurn, carId, crashed = carsById[carId]
        if crashed:
            continue
        #print carId
        if direction == 'v':
            if track[row, col] == '|':
                row += 1
            elif track[row, col] == '+':
                if nextTurn == 'L':
                    direction = '>'
                    col += 1
                    nextTurn = 'M'
                elif nextTurn == 'M':
                    row += 1
                    nextTurn = 'R'
                else: 
                    col -= 1
                    nextTurn = 'L'
                    direction = '<'
            elif track[row, col] == '/':
                direction = '<'
                col -= 1
            elif track[row, col] == '\\':
                direction = '>'
                col += 1

            # see if there is a crash, if so, mark the cars as crashed
            crashed = isACrash(row, col)
            carsById[carId] = (row, col, direction, nextTurn, carId, False)           
            if crashed:
                ids = crashTheCars(row, col)
                print 'Crash! at', (row, col), 'cars:', ids, 'steps: ', steps

        elif direction == '^':
            if track[row, col] == '|':
                row -= 1
                #print 'here i am', carId
            elif track[row, col] == '+':
                if nextTurn == 'L':
                    direction = '<'
                    col -= 1
                    nextTurn = 'M'
                elif nextTurn == 'M':
                    row -= 1
                    nextTurn = 'R'
                else: 
                    direction = '>'
                    col += 1
                    nextTurn = 'L'
            elif track[row, col] == '/':
                direction = '>'
                col += 1
            elif track[row, col] == '\\':
                direction = '<'
                col -= 1

            # see if there is a crash, if so, mark the cars as crashed
            crashed = isACrash(row, col)
            carsById[carId] = (row, col, direction, nextTurn, carId, False)           
            if crashed:
                ids = crashTheCars(row, col)
                print 'Crash! at', (row, col), 'cars:', ids, 'steps: ', steps

        elif direction == '>':
            if track[row, col] == '-':
                col += 1
            elif track[row, col] == '+':
                if nextTurn == 'L':
                    direction = '^'
                    row -= 1
                    nextTurn = 'M'
                elif nextTurn == 'M':
                    col += 1
                    nextTurn = 'R'
                else: # 'R'
                    direction = 'v'
                    row += 1
                    nextTurn = 'L'
            elif track[row, col] == '/':
                direction = '^'
                row -= 1
            elif track[row, col] == '\\':
                direction = 'v'
                row += 1

            # see if there is a crash, if so, mark the cars as crashed
            crashed = isACrash(row, col)
            carsById[carId] = (row, col, direction, nextTurn, carId, False)           
            if crashed:
                ids = crashTheCars(row, col)
                print 'Crash! at', (row, col), 'cars:', ids, 'steps: ', steps

        elif direction == '<':
            if track[row, col] == '-':
                col -= 1
            elif track[row, col] == '+':
                if nextTurn == 'L':
                    direction = 'v'
                    row += 1
                    nextTurn = 'M'
                elif nextTurn == 'M':
                    col -= 1
                    nextTurn = 'R'
                else: # 'R'
                    direction = '^'
                    row -= 1
                    nextTurn = 'L'
            elif track[row, col] == '/':
                direction = 'v'
                row += 1
            elif track[row, col] == '\\':
                direction = '^'
                row -= 1

            # see if there is a crash, if so, mark the cars as crashed
            crashed = isACrash(row, col)
            carsById[carId] = (row, col, direction, nextTurn, carId, False)           
            if crashed:
                ids = crashTheCars(row, col)
                print 'Crash! at', (row, col), 'cars:', ids, 'steps: ', steps

    #printTrack()
    if len(carsById) - countCrashedCars(carsById) == 1:
        print 'found last car!'
        for row, col, direction, nextTurn, carId, crashed in carsById.values():
            #print carId, row, col, crashed
            if not crashed:
                print carId, row, col, direction, track[row, col]
                print col, row

        exit()


    steps += 1
    if steps > 20000:
        exit()

print "Answer is the car that is not crashed (4th item is False)."