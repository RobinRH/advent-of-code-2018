# 38380
#
# https://adventofcode.com/2018/day/6

import sys
import numpy as np 
import pprint
import csv


with open(sys.argv[1]) as csv_file:
    points = [(int(row[0]), int(row[1])) for row in csv.reader(csv_file, delimiter=',')]

size = 1000
array = np.zeros((size,size), dtype = np.int)

for row in range(size):
    for col in range(size):
        total = sum([abs(col-pCol) + abs(row-pRow) for pRow, pCol in points])
        if total < 10000:
            array[row, col] = 1

print np.sum(array)