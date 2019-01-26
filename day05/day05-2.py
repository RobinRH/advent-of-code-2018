# 5534
#
# https://adventofcode.com/2018/day/5


import sys
import string

with open(sys.argv[1], 'r') as polymerFile:
    polymer = polymerFile.read()

lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
n = len(lower)

# make a list of strings like 'aA', 'Aa', 'bB', 'Bb'
replacements = []
for i in range(0, n):
    replacements.append((lower[i] + upper[i]))
    replacements.append((upper[i] + lower[i]))


def findCompressedLength(strpolymer):
    found = True
    while found:
        length = len(strpolymer)
        for r in replacements:
            strpolymer = strpolymer.replace(r, "")
        newLength = len(strpolymer)
        if length == newLength:
            found = False

    return len(strpolymer)

lengths = []
for i in range(0, n):
    shorter = polymer.replace(lower[i], "").replace(upper[i], "")
    lengths.append(findCompressedLength(shorter))

print min(lengths)

