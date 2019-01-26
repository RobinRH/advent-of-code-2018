# 2049
#
# https://adventofcode.com/2018/day/12

import sys
import numpy as np 
import re
from collections import Counter
import pprint

def getCount(arow, initial):
    length = len(arow)
    final = list(arow)
    inputLength = len(initial)
    sum = 0
    for col in range(length):
        if final[col] == '#':
            sum += (col - 2 * inputLength)
    
    return sum

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

rows = []
# create a string 3 times as long as the input string
first = list(('.' * len(initial) * 2) + initial + ('.' * len(initial) * 2))
rows.append(first)
for i in range(1, 21):
    second = list('.' * len(first))
    for col in range(2, len(first) - 3):
        inFirst = ''.join(first[col-2: col + 3])
        if inFirst in rules.keys():
            second[col] = rules[inFirst]
        else:
            second[col] = '.'
    rows.append(second)
    first = second

print getCount(rows[-1], initial)

