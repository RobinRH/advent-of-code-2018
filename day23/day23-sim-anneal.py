# 12298 is too low
# 68989 is too low
# 401785 too low
# https:#adventofcode.com/2018/day/23

import sys

import numpy as np 
import re
from collections import Counter
from pprint import pprint
from collections import namedtuple
from random import randint
import math
import random

######## read lines in file
with open(sys.argv[1], 'r') as inputFile:
    lines = map(lambda s: s.strip().replace('pos=<', '').replace(',', ' ').replace('>  r=', ' '), list(inputFile))

#pos=<0,0,0>, r=4
# x, y, z, radius

points = []
Point = namedtuple('Point', 'x y z radius')
for line in lines:
    ints = line.split(' ')
    ints  = [int(x) for x in ints]
    p = Point(ints[0], ints[1], ints[2], ints[3])
    points.append(p)



def distance(p1, p2):
    return abs(p1.x-p2.x) + abs(p1.y - p2.y) + abs(p1.z - p2.z)

def getMinMax():
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    zs = [p[2] for p in points]
    rs = [p[3] for p in points]

    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    zmin, zmax = min(zs), max(zs)
    rmin, rmax = min(rs), max(rs)

    return xmin, xmax, ymin, ymax, zmin, zmax, rmin, rmax

def getRandomPoint():
    return 1

# java version from https://www.geeksforgeeks.org/simulated-annealing/
# Initial and final temperature 
T = .9
# Temperature at which iteration terminates 
Tmin = .0001
# Decrease in temperature 
alpha = 0.9; 
# Number of iterations of annealing 
# before decreasing temperature 
numIterations = 100

def getNeighbor(p, temp):
    temp = int(temp * 10000000) 
    xdiff = randint(-1 * temp,1 * temp)
    ydiff = randint(-1 * temp,1 * temp)
    zdiff = randint(-1 * temp,1 * temp)
    newPoint = Point(p.x + xdiff, p.y + ydiff, p.z + zdiff, 0)
    return newPoint

def evaluateSolution(solution):
    # looking for a minimum
    # how many nanobots contain this point

    total = 0
    for point in points:
        if distance(point, solution) <= point.radius:
            total += 1

    return len(points) - total


def runSim(start):

    global T
    global Tmin
    # Set of all possible candidate locations 

    currentSol = start
    currentMinimum = evaluateSolution(currentSol)
    print currentMinimum

    # Continues annealing until reaching minimum temprature 
    while (T > Tmin):

        for i in range(0, numIterations):
            # Reassigns global minimum accordingly 
            if (evaluateSolution(currentSol)):
                currentMinimum = currentSol

            newSol = getNeighbor(currentSol, T); 
            neweval = evaluateSolution(newSol)

            ap = math.pow(math.e, (evaluateSolution(currentSol) - evaluateSolution(newSol))/T)
            if ap > random.uniform(0,1):
                currentSol = newSol

        T *= alpha; # Decreases T, cooling phase 

        return currentMinimum


instructions = '''
run the app
the minimum will want to settle at 107 (993 nanobots in the solution)
but the true minimum is 82
you can change the starting point and tweak T, Tmin, and numIterations
to stay in the neighborhood
once you have a point in the final neighborhood, copy it over to 
the day23-2.py file
'''

print instructions
apoint = Point(x=60240575, y=23337911, z=23302487, radius=0)
apoint = Point(x=0, y=0, z=0, radius=0)
answer = runSim(apoint)

while evaluateSolution(answer) > 82:
    answer = runSim(answer)
    print answer, evaluateSolution(answer), distance(answer, Point(0,0,0,0))

print answer

'''
 example points
# Point(x=60223411, y=23320941, z=23268354, radius=0) 106812706 106812706
# Point(x=60224311, y=23321598, z=23269912, radius=0) 106815821 106815821
# Point(x=60225380, y=23321827, z=23271208, radius=0) 106818415 106818415
# Point(x=60226357, y=23322727, z=23273084, radius=0) 106822168 106822168
# Point(x=60227105, y=23323390, z=23274496, radius=0) 106824991 106824991
# Point(x=60227309, y=23323365, z=23274676, radius=0) 106825350 106825350
# Point(x=60228216, y=23324318, z=23276535, radius=0) 106829069 106829069
# Point(x=60228827, y=23325170, z=23277998, radius=0) 106831995 106831995
# Point(x=60228827, y=23325170, z=23277998, radius=0) 106831995 106831995
# Point(x=60229957, y=23326710, z=23280669, radius=0) 106837336 106837336
# Point(x=60230995, y=23328007, z=23283004, radius=0) 106842006 106842006
# Point(x=60232305, y=23329256, z=23285563, radius=0) 106847124 106847124
# Point(x=60233253, y=23330659, z=23287916, radius=0) 106851828 106851828
# Point(x=60234614, y=23331403, z=23290018, radius=0) 106856035 106856035
# Point(x=60235646, y=23332602, z=23292248, radius=0) 106860496 106860496
# Point(x=60236545, y=23333590, z=23294135, radius=0) 106864270 106864270
# Point(x=60237231, y=23334223, z=23295455, radius=0) 106866909 106866909
# Point(x=60237874, y=23334730, z=23296607, radius=0) 106869211 106869211
# Point(x=60238513, y=23334865, z=23297382, radius=0) 106870760 106870760 
# Point(x=60238969, y=23335494, z=23298465, radius=0) 106872928 106872928
# Point(x=60239745, y=23335605, z=23299351, radius=0) 106874701 106874701
# Point(x=60240054, y=23336496, z=23300554, radius=0) 106877104 106877104
# Point(x=60240066, y=23337020, z=23301087, radius=0) 106878173 106878173
# Point(x=60240575, y=23337911, z=23302487, radius=0) 82        106880973
# Point(x=60247420, y=23331398, z=23302822, radius=0) 82 106881640
# Point(x=60243984, y=23336591, z=23304575, radius=0) 82 106885150
# Point(x=60250654, y=23336151, z=23310809, radius=0) 82 106897614, getting this repeatedly
# Point(x=59474888, y=22737864, z=22288295, radius=0) 83 104501047, getting this repeatedly
# Point(x=59482693, y=22820356, z=22198029, radius=0) 88 104501078


# Point(x=59499872, y=22472252, z=22832036, radius=0) 107 104804160
# Point(x=59580679, y=21945776, z=23205444, radius=0) 107 104731899
# Point(x=58689678, y=23308964, z=22575821, radius=0) 107 104574463 not correct
Point(x=5277974, y=3494166, z=311744, radius=0)
888 Point(x=7943516, y=4614869, z=2343000, radius=0)
879 Point(x=10444130, y=4790976, z=3777711, radius=0)
866 Point(x=13361322, y=6090300, z=6572750, radius=0)
848 Point(x=17316788, y=8148034, z=8521131, radius=0) 848 
834 Point(x=20230437, y=10604171, z=9648907, radius=0)
818 Point(x=23871197, y=15343563, z=10683827, radius=0)
803 Point(x=28648874, y=15954580, z=11628943, radius=0)
790 Point(x=31614049, y=14985750, z=14246744, radius=0)
'''
