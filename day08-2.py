# 33649
#
# https://adventofcode.com/2018/day/8

import sys
sys.setrecursionlimit(4000)

def readNumbers(numbers):

    if not numbers:
        return 0

    # pop off the first two
    nChildren = numbers.pop(0)
    nMetadata = numbers.pop(0)

    if nChildren == 0:
        sumMetadata = 0
        for i in range(nMetadata):
            sumMetadata += numbers.pop(0)
        return sumMetadata

    # now read the the children
    childrenMetadata = []
    for nc in range(nChildren):
        childrenMetadata.append(readNumbers(numbers))

    # what's left is the metadata
    sumMeta = 0
    for i in range(nMetadata):
        childIndex = numbers.pop(0)
        if childIndex <= len(childrenMetadata):
            sumMeta += childrenMetadata[childIndex-1]

    return sumMeta

if __name__ == "__main__": 

    with open(sys.argv[1], 'r') as inputFile:
        allNumbers = [int(s) for s in inputFile.read().split(' ')]

    print readNumbers(allNumbers)
