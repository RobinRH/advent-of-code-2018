# 20,68 
#
# https://adventofcode.com/2018/day/11

import sys
import numpy as np 
import pprint

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


# test cases
#print getCellPower(5,3, 8), 4
#print getCellPower(79, 122, 57), -5
#print getCellPower(196, 217, 39), 0
#print getCellPower(153, 101, 71), 4

serialNumber = 5791
gridWithPower = getGridWithPowers(serialNumber)

sums = np.zeros((300, 300), dtype = np.int32)
for row in range(297):
    for col in range(297):
        sums[row, col] = np.sum(gridWithPower[row:row+3, col:col+3])

# gets the coordinates of the cell with the highest power
print tuple(reversed(np.unravel_index(sums.argmax(), sums.shape)))



