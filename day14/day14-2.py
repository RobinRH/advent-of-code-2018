# 20236441 
# takes a while to run
# https://adventofcode.com/2018/day/14

import sys

scores = [3,7]

def getNextRecipes(a, b):
    sumString = str(a + b)
    digits = [int(x) for x in list(sumString)]
    return digits

def getNextLocation(location, score, arrayLen):
    newLoc = location + score + 1
    if newLoc >= arrayLen:
        newLoc -= arrayLen
    return newLoc


aLocation = 0
aScore = 3

bLocation = 1
bScore = 7

input = '51589' #9
input = '59414' # 2018
input = '920831'

inputArray = [int(s) for s in list(input)]
scores.extend(getNextRecipes(3,7))
aLocation = 0
bLocation = 1
li = len(input)
inputLength = -1 * len(input)
ls = 0
printNextScore = False
while True:
    aScore = scores[aLocation]
    bScore = scores[bLocation]
    sum = aScore + bScore
    if sum >= 10:
        #scores.extend([1, sum % 10])
        scores.append(1)
        scores.append(sum - 10)
    else:
        scores.append(sum) 
    ls = len(scores)
 
    aLocation += (aScore + 1)
    if aLocation >= ls:
        aLocation -= ls

    bLocation += (bScore + 1)
    if bLocation >= ls:
        bLocation -= ls

    if printNextScore:
        print scores[-10:]
        printNextScore = False

    last6 = scores[(inputLength-1):]
    last6 = last6[0:li]
    if last6 == inputArray:
        print 'found', len(scores) - li - 1
        break


    last5 = scores[inputLength:]
    if last5 == inputArray:
        print 'found', len(scores) - li
        break 


