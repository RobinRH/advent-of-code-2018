# 472
#
# https://adventofcode.com/2018/day/16

import sys
import numpy as np 
import re
from collections import Counter
import pprint

with open(sys.argv[1], 'r') as inputFile:
    lines = map(lambda s: s.strip(), list(inputFile))

firstInstruction = 3138
instructions = lines[firstInstruction:]

linesToRead = 4 # test
linesToRead = 3136 # real
#linesToRead = 12
# 2 2 3 3
lines = lines[0:linesToRead]


#Before: [3, 2, 1, 1]
#9 2 1 2
#After:  [3, 2, 2, 1]

ntests = linesToRead / 4
tests = []
for i in range(ntests):
    before = lines[i * 4].replace('Before: [','').replace(']','')
    opcode = lines[i * 4 + 1]
    after = lines[i * 4 + 2].replace('After:  [','').replace(']', '')

    before = [int(x) for x in before.split(', ')]
    opcode = [int(x) for x in opcode.split(' ')]
    after = [int(x) for x in after.split(', ')]

    tests.append([before, opcode, after])

registers = [0,0,0,0]

#Addition:
def addr(a, b, c):
    #addr (add register) stores into register C the result of adding register A and register B.
    registers[c] = registers[a] + registers[b]
    
def addi(a, b, c):
    #addi (add immediate) stores into register C the result of adding register A and value B.
    registers[c] = registers[a] + b

#Multiplication:
def mulr(a, b, c):
    #mulr (multiply register) stores into register C the result of multiplying register A and register B.
    registers[c] = registers[a] * registers[b]

def muli(a, b, c):
    #muli (multiply immediate) stores into register C the result of multiplying register A and value B.
    registers[c] = registers[a] * b

#Bitwise AND:
def banr(a, b, c):
    #banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
    registers[c] = registers[a] & registers[b]

def bani(a,b,c):
    #bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
    registers[c] = registers[a] & b

#Bitwise OR:
def borr(a, b, c):
    #borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
    registers[c] = registers[a] | registers[b]

def bori(a, b, c):
    #bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
    registers[c] = registers[a] | b

#Assignment:
def setr(a, b, c):
    #setr (set register) copies the contents of register A into register C. (Input B is ignored.)
    registers[c] = registers[a]

def seti(a, b, c):
    #seti (set immediate) stores value A into register C. (Input B is ignored.)
    registers[c] = a

#Greater-than testing:
def gtir(a, b, c):
    #gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
    registers[c] = 1 if a > registers[b] else 0

def gtri(a, b, c):
    #gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
    registers[c] = 1 if registers[a] > b else 0

def gtrr(a, b, c):
    #gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.
    registers[c] = 1 if registers[a] > registers[b] else 0

#Equality testing:
def eqir(a, b, c):
    #eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
    registers[c] = 1 if a == registers[b] else 0

def eqri(a, b, c):
    #eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
    registers[c] = 1 if registers[a] == b else 0

def eqrr(a, b, c):
    #eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.
    registers[c] = 1 if registers[a] == registers[b] else 0

opcodes = [
    addr,
    addi,
    mulr,
    muli,
    banr,
    bani,
    borr,
    bori,
    setr,
    seti,
    gtir,
    gtri,
    gtrr,
    eqir,
    eqri,
    eqrr
]


# to do a test run
# set up the registers
# run each op code
# compare to the output
possibles = {}
for i in range(16):
    possibles[i] = set(range(16))


threeOrMore = 0
for before, instruction, after in tests:
    success = 0
    s = set()
    for op in range(len(opcodes)):
        for i in range(4):
            registers[i] = before[i]
        opcodes[op](instruction[1], instruction[2], instruction[3])
        passed = True
        for i in range(4):
            if registers[i] != after[i]:
                passed = False
        if passed:
            s.add(op)
            success += 1
    possibles[instruction[0]] = possibles[instruction[0]].intersection(s)


    if success >= 3:
        threeOrMore += 1


# now the process of elimination, for example 11 is 12, so remove 12 from all other groups
results = []
done = False
while len(results) < len(opcodes):
    # there will be one that has only one option, find it
    pair = (0,0)
    for key in possibles.keys():
        if len(possibles[key]) == 1:
            pair = (key, list(possibles[key])[0])
            results.append(pair)
            break
    # now that you have that one, remove it from the other lists
    for value in possibles.values():
        if pair[1] in value:
            value.remove(pair[1])



lookup = {}
for instructionNum, opcodeNum in results:
    lookup[instructionNum] = opcodeNum

# check if all tests pass, using possibles


numPassed = 0
numFailed = 0
for before, instruction, after in tests:
    for i in range(4):
        registers[i] = before[i]
    # the opcode is the same as opcode[0]
    operatorNum = lookup[instruction[0]]
    operator = opcodes[operatorNum]
    operator(instruction[1], instruction[2], instruction[3])
    passed = True
    for i in range(4):
        if registers[i] != after[i]:
            passed = False
    if passed: 
        numPassed += 1
    else:
        numFailed += 1


# now run the instructions
registers = [0,0,0,0]
for inst in instructions:
    codes = [int(x) for x in inst.split(' ')]
    opnumber = lookup[codes[0]]
    operator = opcodes[opnumber]
    operator(codes[1], codes[2], codes[3])

print registers[0]