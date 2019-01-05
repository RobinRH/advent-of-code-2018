# GKPTSLUXBIJMNCADFOVHEWYQRZ
# 
# https://adventofcode.com/2018/day/7

import sys
import numpy as np 
import re
from collections import Counter
import pprint
import string

with open(sys.argv[1], 'r') as inputFile:
    lines = [s.strip().replace('Step ', '').replace('must be finished before step ','').replace(' can begin.','') for s in list(inputFile)]

rules = [line.split(' ') for line in lines]
nodes = set([rule[0] for rule in rules]).union(set([rule[1] for rule in rules]))

ancestors = { x: [] for x in nodes}

for rule in rules:
    ancestors[rule[1]].append(rule[0])

finished = rules[0][0]

order = ''
while len(ancestors) > 0:

    # find all the nodes that have no ancestors (nodes that aren't dependent on another node)
    possibles = [a for a in ancestors.keys() if len(ancestors[a]) == 0]

    if len(possibles) == 0:
        nextLetter = None
    elif len(possibles) == 1:
        nextLetter = possibles[0]
    else:
        nextLetter = sorted(possibles)[0]

    if nextLetter:
        ancestors.pop(nextLetter)
        order += nextLetter
        for b in ancestors.keys():
            if nextLetter in ancestors[b]:
                ancestors[b].remove(nextLetter)


print order

'''
{'A': ['C', 'I', 'K', 'J'],
 'B': ['X', 'G'],
 'C': ['N', 'P', 'J', 'U'],
 'D': ['G', 'N'],
 'E': ['D', 'F', 'A', 'M', 'X', 'H'],
 'F': ['B', 'U', 'N'],
 'H': ['K', 'J', 'N', 'V', 'G', 'D', 'C'],
 'I': ['G', 'T', 'X'],
 'J': ['P', 'X', 'I'],
 'L',
 'M': ['J'],
 'N': ['I'],
 'O': ['G', 'J', 'A', 'D', 'I', 'F', 'P'],
 'Q': ['M', 'V', 'W', 'Y', 'N', 'D', 'B', 'O', 'A'],
 'R': ['J', 'Q', 'H', 'Y', 'M', 'O'],
 'S',
 'T',
 'U': ['P'],
 'V': ['N', 'B', 'I', 'K'],
 'W': ['I', 'U', 'O', 'M', 'C'],
 'X': ['T', 'G'],
 'Y': ['A', 'O', 'E', 'B', 'V', 'W', 'X', 'H'],
 'Z': ['H', 'Y', 'R', 'P', 'I', 'E', 'Q', 'F', 'W', 'M', 'V']}
 '''