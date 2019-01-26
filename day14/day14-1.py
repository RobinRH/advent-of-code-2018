# 7121102535 
#
# https://adventofcode.com/2018/day/14

import sys
import numpy as np 
import re
from collections import Counter
import pprint


scores = [3,7]

def getNextRecipes(a, b):
    sum = a + b
    sumString = str(sum)
    digits = [int(x) for x in list(sumString)]
    return digits

def getNextLocation(location, score):
    newLoc = location
    for x in range(score + 1):
        newLoc += 1
        if newLoc == len(scores):
            newLoc = 0
    return newLoc


aLocation = 0
aScore = 3

bLocation = 1
bScore = 7

scores.extend(getNextRecipes(3,7))
aLocation = getNextLocation(aLocation, aScore)
bLocation = getNextLocation(bLocation, bScore)

while len(scores) < 930831:
    aScore = scores[aLocation]
    bScore = scores[bLocation]
    scores.extend(getNextRecipes(aScore, bScore))
    aLocation = getNextLocation(aLocation, aScore)
    bLocation = getNextLocation(bLocation, bScore)


# after 9 recipes
scores9 = scores[9:19]
x = [str(a) for a in scores9]
x = int(''.join(x))
print "Test 1: ", x == 5158916779

scores9 = scores[5:15]
x = [str(a) for a in scores9]
x = ''.join(x)
print "Test 2: ", x == '0124515891'

scores9 = scores[18:28]
x = [str(a) for a in scores9]
x = ''.join(x)
print "Test 3: ", x == '9251071085'

scores9 = scores[2018:2028]
x = [str(a) for a in scores9]
x = ''.join(x)
print "Test 4: ", x == '5941429882'


scores9 = scores[920831:(920831+10)]
x = [str(a) for a in scores9]
x = ''.join(x)
print x


