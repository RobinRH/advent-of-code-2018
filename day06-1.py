# 3276
#
# https://adventofcode.com/2018/day/6

import sys
import numpy as np 
import pprint
from collections import Counter
import csv


def getClosestPoint(pRow, pCol):
    distances = [abs(col-pCol) + abs(row-pRow) for row, col in points]
    minDistance = min(distances)
    howMany = distances.count(minDistance)
    if howMany == 1:
        return distances.index(minDistance)
    else:
        return -1

if __name__ == "__main__": 

    with open(sys.argv[1]) as csv_file:
        points = [(int(row[0]), int(row[1])) for row in csv.reader(csv_file, delimiter=',')]

    size = 400  # fortunately, don't need to look into negative indexes to find the correct answer

    array = np.zeros((size,size), dtype = np.int)

    for row in range(size):
        for col in range(size):
            array[row, col] = getClosestPoint(row, col)

    counts = Counter(list(array.flatten()))     # count up occurences of each "letter"

    # anyone not on the perimeter is blocked
    perimeter = list(array[0, :]) + list(array[:, 0]) + list(array[-1, :]) + list(array[:, -1])

    onPerimeter = Counter(perimeter)    # get unique list of "letters" on the perimeter

    landlocked = set(counts.keys()) - set(onPerimeter.keys())
    print max([counts[locked] for locked in landlocked])

