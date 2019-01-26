# 42196
#
# https://adventofcode.com/2018/day/8

import sys
sys.setrecursionlimit(4000)

def readNumbers(numbers):
    global nodes
    global children
    global letter

    if len(numbers) == 0:
        return
    # pop off the first two
    nChildren = numbers.pop(0)
    nMetadata = numbers.pop(0)
    children += nChildren
    nodes += nChildren

    if nChildren == 0:
        for i in range(nMetadata):
            metadata.append(numbers.pop(0))
        return

    # now read the the children
    for nc in range(nChildren):
        readNumbers(numbers)

    # what's left is the metadata
    for i in range(nMetadata):
        metadata.append(numbers.pop(0))


if __name__ == "__main__": 

    with open(sys.argv[1], 'r') as inputFile:
        allNumbers = [int(s) for s in inputFile.read().split(' ')]

    # 2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2

    metadata = []
    nodes = 0
    children = 0

    readNumbers(allNumbers)
    print 'nodes', nodes
    print 'children', children
    print len(metadata)
    print sum(metadata)
