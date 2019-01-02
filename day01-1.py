# 516
#
# https://adventofcode.com/2018/day/1

import sys

with open(sys.argv[1], 'r') as inputFile:
    numbers = sum([int(x) for x in inputFile.readlines()])

print numbers
