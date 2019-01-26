# 373597, 2954067253
#
# https://adventofcode.com/2018/day/9

import sys
import pprint

class Node:
    def __init__(self, num, nxt, prv):
        self.number = num
        self.next = nxt
        self.previous = prv

def printLoop(circleRoot):
    output = ''
    end = circleRoot
    output += str(circleRoot.number)
    circleRoot = circleRoot.next
    while not circleRoot is end:
        output += ' ' + str(circleRoot.number)
        circleRoot = circleRoot.next
    print output

def addNumber(n, current):
    # move ahead 1
    c1 = current.next
    c2 = current.next.next

    newNode = Node(n, c2, c1)
    c1.next = newNode
    c2.previous = newNode

    return newNode    

def handle23(current):
    # remove marble 7 back
    for i in range(7):
        current = current.previous
    
    previous = current.previous
    nextn = current.next
    previous.next = nextn
    nextn.previous = previous
    # current marble is next after the remove marble
    newCurrent = nextn
    # return the new current and the value of the removed marble
    return newCurrent, current.number

def playGame(numPlayers, numMarbles):
    root = Node(0, None, None)
    root.next = root
    root.previous = root
    current = root
    p = 1
    players = numPlayers * [0]
    for i in range(1, numMarbles + 1):
        if i % 23 != 0:
            current = addNumber(i, current)
        else:
            current, points = handle23(current)
            players[p] += i
            players[p] += points
        p += 1
        if p == numPlayers:
            p = 0
    return max(players)


if __name__ == "__main__": 

    with open(sys.argv[1], 'r') as inputFile:
        testLines = list(inputFile)

    tests = []
    # 9 players; last marble is worth 25 points: high score is 32
    for line in testLines:
        tokens = line.split(' ')
        tests.append((int(tokens[0]), int(tokens[6]), int(tokens[11])))

    for nPlayers, nMarbles, highScore in tests:
        high = playGame(nPlayers, nMarbles)
        print high, 'passed' if high == highScore else 'failed'


