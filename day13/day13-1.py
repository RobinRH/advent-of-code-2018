# 43,91 (col, row)
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

track = np.array(list(' ' * rows * cols)).reshape((rows, cols))

def printTrack(track, cars):
    printTrack = np.copy(track)
    for car in cars.keys():
        row, col, direction, nextTurn = cars[car]
        printTrack[row, col] = direction

    for row in printTrack:
        print ''.join(row)

    print

cars = {}
carCount = 0
for r in range(len(lines)):
    row = list(lines[r])
    for c in range(len(row)):
        track[r, c] = row[c]
        if row[c] == 'v':
            cars[r*1000 + c] = (r, c, 'v', 'L')
            carCount += 1
            track[r, c] = '|'
        elif row[c] == '^':
            cars[r*1000 + c] = (r, c, '^', 'L')
            carCount += 1
            track[r, c] = '|'
        elif row[c] == '>':
            cars[r*1000 + c] = (r, c, '>', 'L')
            carCount += 1
            track[r, c] = '-'
        elif row[c] == '<':
            cars[r*1000 + c] = (r, c, '<', 'L')
            carCount += 1
            track[r, c] = '-'


steps = 0
while True:
    newCars = {}
    carKeys = list(sorted(cars.keys()))
    oldKeys = []
    for ck in carKeys:
        oldKeys.append(ck)

    for car in carKeys:
        row, col, direction, nextTurn = cars[car]
        oldKeys.remove(car)
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

            if (row * 1000 + col) in newCars.keys() or (row * 1000 + col in oldKeys):
                print 'Crash!', col, row
                exit()
            else:
                newCars[row * 1000 + col] = (row, col, direction, nextTurn)           
        elif direction == '^':
            if track[row, col] == '|':
                row -= 1
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

            if (row * 1000 + col) in newCars.keys() or (row * 1000 + col in oldKeys):
                print 'Crash!', col, row
                exit()
            else:
                newCars[row * 1000 + col] = (row, col, direction, nextTurn)           
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

            if (row * 1000 + col) in newCars.keys() or (row * 1000 + col in oldKeys):
                print 'Crash!', col, row
                exit()
            else:
                newCars[row * 1000 + col] = (row, col, direction, nextTurn)           
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

            if (row * 1000 + col) in newCars.keys() or (row * 1000 + col in oldKeys):
                print 'Crash!', col, row
                exit()
            else:
                newCars[row * 1000 + col] = (row, col, direction, nextTurn)           

    cars = newCars
    steps += 1
    if steps > 1000:
        break



