# 71892
#
# https://adventofcode.com/2018/day/1

import sys

with open(sys.argv[1], 'r') as inputFile:
    #numbers = map((lambda x : int(x)), inputFile.readlines())
    numbers = [int(x) for x in inputFile.readlines()]


visited = set([0])

i = 0
current = 0
found = False
while not found:
    current += numbers[i]
    if current in visited:
        found = True
    else:
        visited.add(current)
    i += 1
    if i == len(numbers):
        i = 0

print current
