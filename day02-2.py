# kbqwtcvzhmhpoelrnaxydifyb
# 
# https://adventofcode.com/2018/day/2

import sys

with open(sys.argv[1], 'r') as inputFile:
    lines = [s.strip() for s in list(inputFile)]

for a in lines:
    for b in lines:
        common = [a[i] for i in range(len(a)) if a[i] == b[i]]
        if len(a) - len(common) == 1:
            print ''.join(common)
            exit()
