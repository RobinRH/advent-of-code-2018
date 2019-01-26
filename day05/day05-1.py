# 9296
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

found = True
while found:
    length = len(polymer)
    for r in replacements:
        polymer = polymer.replace(r, "")
    newLength = len(polymer)
    if length == newLength:
        found = False

print len(polymer)
