# 1068
#
# https://adventofcode.com/2018/day/22

import numpy as np 
from pprint import pprint
from collections import namedtuple

Location = namedtuple('Location', 'y x gear torch')

def printCavern():
    for row in cavern:
        print ''.join([legend[x] for x in row])

def getGeoIndex(y, x):

    if (y, x) == (0 , 0):
        #The region at 0,0 (the mouth of the cave) has a geologic index of 0.
        return 0
    elif (y, x) == target:
        #The region at the coordinates of the target has a geologic index of 0.
        return 0
    elif y == 0:
        #If the region's Y coordinate is 0, the geologic index is its X coordinate times 16807.
        return 16807 * x
    elif x == 0:
        #If the region's X coordinate is 0, the geologic index is its Y coordinate times 48271.
        return 48271 * y
    else:
        #Otherwise, the region's geologic index is the result of multiplying the erosion levels of the regions at X-1,Y and X,Y-1.
        return erosions[y, x-1] * erosions[y-1, x]

def getErosionLevel(y, x):
    # A region's erosion level is its geologic index plus the cave system's depth, all modulo 20183. 
    return (getGeoIndex(y, x) + depth) % 20183

def getType(erosionLevel):
    #If the erosion level modulo 3 is 0, the region's type is rocky.
    #If the erosion level modulo 3 is 1, the region's type is wet.
    #If the erosion level modulo 3 is 2, the region's type is narrow.
    if erosionLevel % 3 == 0:
        return rocky
    elif erosionLevel % 3 == 1:
        return wet
    else:
        return narrow



def manhattanDistance(a, b):
    ay, ax = a[0], a[1]
    by, bx = b[0], b[1]
    return (abs(ay - by) + abs(ax - bx))


def reconstructPath(cameFrom, current):
    path = [current]
    time = 0
    ones = 0
    while not path[-1] == (0,0, False, True):
        nextLoc = cameFrom[path[-1]]
        cost = distanceBetween(path[-1], nextLoc)
        if cost == 1:
            ones += 1
        time += cost
        # if cost == 8:
        #     print path[-1], nextLoc
        path.append(nextLoc)
        #path.append(cameFrom[path[-1]])

    print 'Part 2: ', time
    #print 'ones', ones
    return path

def getLowestFScore(openset, fscore):
    # fscore is dictionary of (y, x) and cost to get to (y, x)
    # openset is an array of (y, x)
    lowestValue = fscore[openset[0]] # pick any random value in fscore
    lowestKey = None
    # find the key for the lowest value
    for key in openset:
        if fscore[key] <= lowestValue:
            lowestValue = fscore[key]
            lowestKey = key
    return lowestKey

def distanceBetween(a, b):
    ya, xa, ga, ta = a
    yb, xb, gb, tb = b
    if (ga == gb) and (ta == tb):
        return 1
    else:
        return 7 + 1



def getNeighbors(location):
    #y, x, g, t = location

    locationType = cavern[location.y, location.x]
    diffs = [(-1,0), (1, 0), (0,-1), (0, 1)]
    neighbors = []
    for ydiff, xdiff in diffs:
        neighbor = Location(location.y + ydiff, location.x + xdiff, location.gear, location.torch)
        if neighbor.x >= 0 and neighbor.y >= 0 and neighbor.x < xsize and neighbor.y < ysize:
            neighborType = cavern[location.y + ydiff, location.x + xdiff]
            if locationType == neighborType:
                neighbor = Location(location.y + ydiff, location.x + xdiff, location.gear,location.torch)
                neighbors.append(neighbor)                
            else:
                tools = toolOptions[(locationType, neighborType)]
                for tool in tools:
                    neighbor = Location(location.y + ydiff, location.x + xdiff, tool[0], tool[1])
                    neighbors.append(neighbor)
        else:
            if neighbor.x == xsize:
                print 'bumped x'
            elif neighbor.y == ysize:
                print 'bumped y'
    return neighbors


# location includes gear and torch
# start is y, x, gear, torch
# pseudo code from wikipedia
def astar(start, goal):
    # The set of nodes already evaluated
    closedSet = set()

    # The set of currently discovered nodes that are not evaluated yet. Initially, only the start node is known.
    openSet = [start] 

    # For each node, which node it can most efficiently be reached from.
    # If a node can be reached from many nodes, cameFrom will eventually contain the
    # most efficient previous step.
    cameFrom = {}

    # For each node, the cost of getting from the start node to that node.
    # gScore := map with default value of Infinity
    gScore = {}

    # The cost of going from start to start is zero.
    gScore[start] = 0

    # For each node, the total cost of getting from the start node to the goal
    # by passing by that node. That value is partly known, partly heuristic. (f = g + h)
    fScore = {}

    # For the first node, that value is completely heuristic.
    # Will use manhattan distance for heuristic
    fScore[start] = manhattanDistance(start, goal)

    while len(openSet) > 0:
        current = getLowestFScore(openSet, fScore)
        if current == goal:
            return reconstructPath(cameFrom, current)

        openSet.remove(current)
        closedSet.add(current)

        neighbors = getNeighbors(current)
        for neighbor in neighbors:
            if neighbor in closedSet:
                continue		# Ignore the neighbor which is already evaluated.

            # The distance from start to a neighbor
            tentative_gScore = gScore[current] + distanceBetween(current, neighbor)

            if not neighbor in openSet:	# Discover a new node
                openSet.append(neighbor)
            elif tentative_gScore >= gScore[neighbor]: # have already found a shorter path
                continue       

            # This path is the best until now. Record it!
            cameFrom[neighbor] = current
            gScore[neighbor] = tentative_gScore
            fScore[neighbor] = gScore[neighbor] + manhattanDistance(neighbor, goal)


if __name__ == "__main__": 

    # real
    depth = 11541
    target = (14,778) # x,y
    target = (778, 14) # y,x

    # test
    # depth = 510
    # target = (10,10)

    # make a big cavern
    ysize = 2 * target[0]
    xsize = 12 * target[1]
    cavern = np.zeros((ysize, xsize), dtype=np.int64)
    erosions = np.zeros((ysize, xsize), dtype=np.int64)
    indexes = types = np.zeros((ysize, xsize), dtype=np.int64)

    rocky = 0
    narrow = 2
    wet = 1

    for y in range(0, ysize):
        for x in range(0, xsize):
            indexes[y,x] = getGeoIndex(y,x)
            erosions[y, x] = getErosionLevel(y, x)
            cavern[y,x] = getType(erosions[y,x])

    # rocky as ., wet as =, narrow as |
    legend = {
        rocky : '.',
        wet : '=',
        narrow: '|'
    }

    #0 for rocky regions, 1 for wet regions, and 2 for narrow regions.

    # just checking - should be 11575
    print "Part 1: ", np.sum(cavern[0:target[0]+ 1, 0:target[1]+1])

    # rocky: gear or torch
    # wet: gear or neither
    # narrow: torch or neither
    toolOptions = {
        (rocky, rocky)   : [(True, False), (False, True)],
        (rocky, wet)     : [(True, False)],
        (rocky, narrow)  : [(False, True)],
        (wet, rocky)     : [(True, False)],
        (wet, wet)       : [(True, False), (False, False)],
        (wet,  narrow)   : [(False, False)],
        (narrow, rocky)  : [(False, True)],
        (narrow, wet)    : [(False, False)],
        (narrow, narrow) : [(False, False) and (False, True)]
    }

    start = Location(0, 0, False, True)
    goal = Location(target[0], target[1], False, True)
    # final result prints out as part of call to astar
    print "Runs for a long time..."
    solution = astar(start, goal)


'''
# will have to account for making different equipment choices at each location
# so there might be 4 * n options at point, each will have a different cost
# so a location is a location + equipment

# Rocky: gear or torch
# Wet: gear or neither
# Narrow: torch or neither
    
current tools
gear, torch
r : 
    True, False
    False, True
w :
    True, False
    False, False
n :
    False, False
    False, True

You can change from one combo to another, but that combo has to be allowed in current location as well
r -> r  neighbor options are (True, False) and (False, True)
r -> w  neighbor options are (True, False)
r -> n  neighbor options are (False, True)
w -> r  neighbor options are (True, False)
w -> w  neighbor options are  (True, False) and (False, False)
w -> n  neighbor options are (False, False)
n -> r  neighbor options are (False, True)
n -> w  neighbor options are (False, False)
n -> n  neighbor options are (False, False) and (False, True)

'''