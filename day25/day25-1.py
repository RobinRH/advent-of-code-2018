# 428
#
# https://adventofcode.com/2018/day/25

import sys

with open(sys.argv[1], 'r') as inputFile:
    lines = [line.strip().split(',') for line in inputFile]

stars = [[int(x) for x in line] for line in lines]

constellations = []
while len(stars) > 0:
    # pick a new star
    constellation = [stars[0]]
    stars.remove(constellation[0])
    newstars = 1
    while newstars > 0: # keep adding stars to the constellation until you can't any more, then create a new constellation
        toremove = []
        for star in stars:
            for c in constellation:
                manDistance = sum(abs(star[i] - c[i]) for i in range(4))
                if manDistance <= 3:
                    if star not in constellation:
                        constellation.append(star)
                        toremove.append(star)
                    continue
                else:
                    pass
        newstars = len(toremove)
        stars = [star for star in stars if star not in toremove]
    constellations.append(constellation)

print len(constellations)