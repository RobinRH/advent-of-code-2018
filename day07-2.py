# 920
# GKPTSXBLIJNUDCMFVAHOEWYQRZ
#
# https://adventofcode.com/2018/day/7

import sys
import numpy as np 
import re
from collections import Counter
import pprint
import string

class Worker:
    def __init__(self):
        self.timer = 0
        self.letter = '.'   # using dot is handy for printing
        self.working = False

    def __repr__(self):
        return ' '.join([str(self.working), self.letter, str(self.timer)])

def getNextLetter():
    # find all the ancestors with no remaining inputs
    possibles = [a for a in ancestors.keys() if len(ancestors[a]) == 0]

    if len(possibles) == 0:
        nextLetter = None
    elif len(possibles) == 1:
        nextLetter = possibles[0]
    else:
        nextLetter = sorted(possibles)[0]

    if nextLetter:
        ancestors.pop(nextLetter)
    return nextLetter


if __name__ == "__main__": 

    with open(sys.argv[1], 'r') as inputFile:
        lines = [s.strip().replace('Step ', '').replace('must be finished before step ','').replace(' can begin.','') for s in list(inputFile)]

    rules = [line.split(' ') for line in lines]
    nodes = set([rule[0] for rule in rules]).union(set([rule[1] for rule in rules]))

    ancestors = { x: [] for x in nodes}

    for rule in rules:
        ancestors[rule[1]].append(rule[0])

    order = ''
    workers = [Worker() for i in range(5)]
    count = 0
    delay = 60
    while len(order) < len(nodes):
        toremove = []

        for worker in workers:
            if not worker.working:
                nl = getNextLetter()
                if nl:
                    worker.letter = nl
                    worker.timer = ord(worker.letter) - ord('A') + delay  # delay A -> 61, B -> 62, etc.
                    worker.working = True
            else:
                worker.timer -= 1

        #print '^'.join(map(lambda w : w.letter, workers))

        for worker in workers:
            if worker.working and worker.timer == 0: 
                order += worker.letter
                for b in ancestors.keys():
                    if worker.letter in ancestors[b]:
                        ancestors[b].remove(worker.letter)
                worker.letter = '.'
                worker.timer = 0
                worker.working = False
        
        #print 'order: ', order

        count += 1
        if count > 10000:
            exit()

    print order
    print count

