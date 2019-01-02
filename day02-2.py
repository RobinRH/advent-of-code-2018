# kbqwtcvzhmhpoelrnaxydifyb
# 
# https://adventofcode.com/2018/day/2

import sys

with open(sys.argv[1], 'r') as inputFile:
    lines = map(lambda s: s.strip(), list(inputFile))

def findab():
    for a in lines:
        for b in lines:
            same = sum([a[i] == b[i] for i in range(len(a))])
            if len(a) - same == 1:
                return a, b

a, b = findab()
common = [a[i] for i in range(len(a)) if a[i] == b[i]]
print ''.join(common)
