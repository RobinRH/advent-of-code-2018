# 231,273,16
#
# https://adventofcode.com/2018/day/11

import sys
import numpy as np 
import pprint
from collections import Counter

#Find the fuel cell's rack ID, which is its X coordinate plus 10.
#Begin with a power level of the rack ID times the Y coordinate.
#Increase the power level by the value of the grid serial number (your puzzle input).
#Set the power level to itself multiplied by the rack ID.
#Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
#Subtract 5 from the power level.
def getCellPower(row, col, serialNumber):
    rackId = col + 10
    powerLevel = rackId * row
    powerLevel += serialNumber
    powerLevel *= rackId
    powerLevel = (abs(powerLevel) / 100) % 10
    powerLevel -= 5
    return powerLevel

def getGridWithPowers(serialNumber):
    output = np.zeros((300, 300), dtype = np.int32)
    for row in range(300):
        for col in range(300):
            output[row, col] = getCellPower(row, col, serialNumber)
    return output

def getSums(grid, cellSize):
    output = np.zeros((300, 300), dtype=np.int32)
    for row in range(300 - cellSize):
        for col in range(300 - cellSize):
            output[row, col] = np.sum(grid[row:row+ cellSize, col: col+cellSize])
    return output

def findMax(input):
    return tuple(np.unravel_index(input.argmax(), input.shape))

serialNumber = 5791
gridWithPower = getGridWithPowers(serialNumber)

maximums = {}
for i in range(1, 300):
    output = getSums(gridWithPower, i)
    maxRow, maxCol = findMax(output)
    maxPower = output[maxRow, maxCol]
    maximums[maxPower] = (maxCol, maxRow, i)
    if maxPower <= 0:
        break

maxCol, maxRow, size = maximums[max(maximums.keys())]
print maxCol, maxRow, size

