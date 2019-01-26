# 245280
#
# https://adventofcode.com/2018/day/15

import sys
from pprint import pprint
import copy
import string

def isElf(unit):
    return unit in elfLetters

def isGoblin(unit):
    return unit in goblinLetters

def isATarget(aunit, bunit):
    return (isElf(aunit) and isGoblin(bunit)) or (isGoblin(aunit) and isElf(bunit))

def printCavern():
    for r in range(nrows):
        #output = ''.join(cavern[r, : ])
        output = ''.join([cavern[(r,col)] for col in range(ncols)])
        # print out hit points for each unit on that row
        for c in range(ncols):
            unit = cavern[(r, c)]
            if isGoblin(unit) or isElf(unit):
                output += ' ' + unit + ':' + str(hitPoints[unit])
        print output
    print

def findOpeningsNearTargets(targetLetters):
    openings = set()
    for row in range(nrows):
        for col in range(ncols):
            if cavern[(row, col)] in targetLetters:
                # look up, down, left, and right
                for rdiff, cdiff in neighbors:
                    if cavern[(row + rdiff, col + cdiff)] == empty:
                        openings.add((row + rdiff, col + cdiff))
    return openings

def distance((arow, acol), (brow, bcol)):
    return abs(arow - brow) + abs(acol - bcol)

def findAllReachableCells(start):
    # find all cells that are reachable from start (row,col)
    visited = set()
    visited.add(start)
    foundMore = True
    while foundMore:
        newFrontier = set()
        for row, col in visited:
            for rdiff, cdiff in neighbors:
                newrc = (row + rdiff, col + cdiff)
                if cavern[newrc] == empty and (not newrc in visited) and (not newrc in newFrontier):
                    newFrontier.add(newrc)
        visited = visited.union(newFrontier)
        if len(newFrontier) == 0:
            foundMore = False
    return visited

def getNeighbors((row, col)):
    return [(row + rdiff, col + cdiff) for (rdiff, cdiff) in neighbors if cavern[(row + rdiff, col + cdiff)] == empty]

# pseudo code from wikipedia
def astar(start, goal):
    visited = set()
    frontier = [start]
    cameFrom = {}
    pathCost = {}
    pathCost[start] = 0   # cost to current point
    heuristicCost = {}         # minimun cost to goal

    heuristicCost[start] = distance(start, goal)

    while len(frontier) > 0:
        current = [key for key, value in heuristicCost.items() if value == min(heuristicCost.values())][0]
        if current == goal:
            return len(reconstructPath(cameFrom, current, start))

        frontier.remove(current)
        del heuristicCost[current]
        visited.add(current)

        neighbors = getNeighbors(current)
        for neighbor in neighbors:
            if neighbor in visited:
                continue

            currentCost = pathCost[current] + distance(current, neighbor)

            if not neighbor in frontier:
                frontier.append(neighbor)
            elif currentCost >= pathCost[neighbor]:
                continue       

            cameFrom[neighbor] = current
            pathCost[neighbor] = currentCost
            heuristicCost[neighbor] = pathCost[neighbor] + distance(neighbor, goal)

def reconstructPath(cameFrom, current, start):
    path = [current]
    while not path[-1] == start:
        path.append(cameFrom[path[-1]])
    return path

def findStartForShortestPath((arow, acol), goal, steps):
    readingOrder = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    for rdiff, cdiff in readingOrder:
        nextRow, nextCol = arow + rdiff, acol + cdiff
        # if unit can move to neighbor and unit can reach goal from neighbor
        if (cavern[(nextRow, nextCol)] == empty) and (goal in findAllReachableCells((nextRow, nextCol))):
            shortest = astar((nextRow, nextCol), goal)
            # looking for path length that is one less than the distance from the unit to the goal
            if shortest == steps - 1:
                return (nextRow, nextCol)

def attack(row, col):
    # find all the targets in range
    unit = cavern[(row, col)]
    targets = [(row + rdiff, col + cdiff) for (rdiff, cdiff) in neighbors if isATarget(unit, cavern[(row + rdiff, col + cdiff)])]

    if len(targets) == 0:
        return None

    # pick targets with fewest hit points
    targetLetters = [cavern[t] for t in targets]
    fewest = min([hitPoints[letter] for letter in targetLetters])
    lowTargets = [t for t in targets if hitPoints[cavern[t]] == fewest]

    # if more than 1 target, find the first one in reading order
    chosen = list(sorted(lowTargets))[0]
    chosenUnit = cavern[chosen]
    hitPoints[chosenUnit] -= 3
    if hitPoints[chosenUnit] <= 0:
        # remove from cavern, no more turns
        targetLetter = cavern[chosen]
        cavern[chosen] = empty
        return targetLetter
    else:
        return None

def takeTurn(row, col):
    # returns the letter of the unit removed
    unit = cavern[(row, col)]
    isElf = unit in elfLetters
    isGoblin = unit in goblinLetters
    targetLetters = elfLetters if isGoblin else goblinLetters
    targets = [(r,c) for r in range(nrows) for c in range(ncols) if cavern[(r,c)] in targetLetters]
    openings = findOpeningsNearTargets(targetLetters)

    # determine if in range of target
    alreadyInRange = False
    for t in targets:
        if distance((row, col), t) == 1:
            alreadyInRange = True

    if alreadyInRange:
        attack(row, col)
    else:
        # find the intersection of what's open and in range and what's reachable
        reachable = findAllReachableCells((row, col))
        headfor = openings.intersection(reachable)
        # find the closest one, according to the many rules
        # find all the shortest paths
        shortestHeadFor = [] # array of all headfor at that shortest path length
        if len(headfor) == 0:
            return None
        # find the distance for each location in headfor
        distances = {hf: astar((row, col), hf) for hf in headfor}    # {key: value for (key, value) in iterable}
        # find the shortest distance
        shortestPathLength = min(distances.values())
        # find all the paths with the minimum distance
        shortestHeadFor = [hf for hf in distances.keys() if distances[hf] == shortestPathLength]

        chosen = list(sorted(shortestHeadFor))[0]

        # once you have chosen the location, find out if there are multiple short routes
        # if more than one route, pick by reading order
        nextSpot = findStartForShortestPath((row, col), chosen, shortestPathLength)

        #move to next spot
        temp = cavern[(row,col)]
        cavern[(row, col)] = empty
        cavern[nextSpot] = temp
        # if it's in range, now it can attack
        # note that it moved, so row, col has changed
        isnowinrange = False
        for t in targets:
            if distance((nextSpot[0], nextSpot[1]), t) == 1:
                isnowinrange = True
        if isnowinrange:
            attack(nextSpot[0], nextSpot[1])

if __name__ == "__main__": 

    with open(sys.argv[1], 'r') as inputFile:
        lines = [line.strip() for line in inputFile.readlines()]
    
    nrows = len(lines)
    ncols = len(lines[0])
    cavern = {}

    wall = '#'
    goblin = 'G'
    elf = 'E'
    empty = '.'
    elfLetters = list(string.ascii_lowercase)
    goblinLetters = list(string.ascii_uppercase)
    hitPoints = {}

    for r in range(nrows):
        for c in range(ncols):
            cavern[(r,c)] = lines[r][c]

    gIndex = 0
    eIndex = 0
    for r in range(nrows):
        for c in range(ncols):
            if cavern[(r,c)] == 'G':
                letter = goblinLetters[gIndex]
                cavern[r,c] = letter
                hitPoints[letter] = 200
                gIndex += 1
            elif cavern[(r,c)] == 'E':
                letter = elfLetters[eIndex]
                cavern[r,c] = letter
                hitPoints[letter] = 200
                eIndex += 1

    printCavern()

    neighbors = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    for rounds in range(250):
        unitOrder = [(r,c) for r in range(nrows) for c in range(ncols) if cavern[(r,c)] in string.ascii_letters]
        for row, col in unitOrder:
            unitRemoved = takeTurn(row, col)  # returns the letter of any unit removed during the turn, or None
            # on any give turn, a unit can be removed, they don't get turns
            if unitRemoved:
                unitOrder.remove(unitRemoved)
            # if there are no more targets, end the game
            elves = [x for x in hitPoints.keys() if (hitPoints[x] > 0) and (x in elfLetters)]
            goblins = [x for x in hitPoints.keys() if (hitPoints[x] > 0) and (x in goblinLetters)]
            hitpointsleft = sum([hitPoints[x] for x in hitPoints.keys() if hitPoints[x] > 0])
            if len(elves) == 0 or len(goblins) == 0:
                # which round, determine if the round is complete, meaning the last unit had a turn
                if (row, col) == unitOrder[-1]:
                    complete = rounds + 1
                else:
                    complete = rounds
                print 'result:', complete * hitpointsleft, 'rounds:', complete, 'hitpoints:', hitpointsleft
                exit()

        printCavern()
