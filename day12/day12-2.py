# 2300000000006

# https://adventofcode.com/2018/day/12

import sys
import numpy as np 
import re
from collections import Counter
import pprint


with open(sys.argv[1], 'r') as inputFile:
    lines = map(lambda s: s.strip(), list(inputFile))

# first line is the input string
# initial state: #..#.#..##......###...###
initial = lines[0].replace('initial state: ', '')

# skip first two lines of input
lines.pop(0)
lines.pop(0)

# ...## => #
rules = {}
for line in lines:
    tokens = line.split(' => ')
    rules[tokens[0]] = tokens[1]

def getCount(arow, initial):
    length = len(arow)
    final = list(arow)
    inputLength = len(initial)
    sum = 0
    for col in range(length):
        if final[col] == '#':
            sum += (col - 2 * inputLength)
    
    return sum

def getPattern(plants):
    # plants is a string
    # find first plant
    plants = ''.join(plants)
    firstPlant = plants.index('#')
    lastPlant = plants.rindex('#')
    pattern = plants[firstPlant: lastPlant + 1]
    return pattern

rows = {}
second = ''
first = list(('.' * len(initial) * 2) + initial + ('.' * len(initial) * 2))
firstPattern = getPattern(first)
firstCount = getCount(first, initial)
rows[firstPattern] = (0, firstCount)
firstTime = 0
secondTime = 0
firstRowCount = 0
difference = 0
for i in range(1, 110):
    second = list('.' * len(first))
    for col in range(2, len(first) - 3):
        inFirst = ''.join(first[col-2: col + 3])
        if inFirst in rules.keys():
            second[col] = rules[inFirst]
        else:
            second[col] = '.'
    rowPattern = getPattern(second)
    rowCount = getCount(second, initial)
    if rowPattern in rows.keys():
        secondTime = i
        firstTime = rows[rowPattern][0] 
        difference = rowCount - rows[rowPattern][1]
        firstRowCount = rows[rowPattern][1]
        break
    rows[rowPattern] = (i, rowCount)
    first = second

print difference * (50000000000 - firstTime) + firstRowCount
