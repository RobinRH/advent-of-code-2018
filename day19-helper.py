# 1728, wrong (too low?)
# not 3
# https://adventofcode.com/2018/day/19
# changes the input to make it more readable so you can figure out what it's doing

import sys
import numpy as np 
import re
from collections import Counter
import pprint

with open(sys.argv[1], 'r') as inputFile:
    lines = map(lambda s: s.strip(), list(inputFile))


# #ip 0
# seti 5 0 1

# read the first line to get the instruction register
line0 = lines[0]
tokens = line0.split(' ')
iRegister = int(tokens[1])
print(iRegister)

# seti 5 0 1
instructions = lines[1:]
print instructions

registers = [0,0,0,0,0,0]

#Addition:
def addr(a, b, c):
    #addr (add register) stores into register C the result of adding register A and register B.
    #registers[c] = registers[a] + registers[b]
    print 'add', registers[a], registers[b], registers[c]

def addi(a, b, c):
    #addi (add immediate) stores into register C the result of adding register A and value B.
    #registers[c] = registers[a] + b
    print 'add', registers[a], b, registers[c]

#Multiplication:
def mulr(a, b, c):
    #mulr (multiply register) stores into register C the result of multiplying register A and register B.
    #registers[c] = registers[a] * registers[b]
    print 'mul', registers[a], registers[b], registers[c]

def muli(a, b, c):
    #muli (multiply immediate) stores into register C the result of multiplying register A and value B.
    #registers[c] = registers[a] * b
    print 'mul', registers[a], b, registers[c]

#Bitwise AND:
def banr(a, b, c):
    #banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
    #registers[c] = registers[a] & registers[b]
    print 'ni'

def bani(a,b,c):
    #bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
    #registers[c] = registers[a] & b
    print 'ban', registers[a], b, registers[c]

#Bitwise OR:
def borr(a, b, c):
    #borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
    #registers[c] = registers[a] | registers[b]
    print 'ni'

def bori(a, b, c):
    #bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
    #registers[c] = registers[a] | b
    print 'bor', registers[a], b, registers[c]

#Assignment:
def setr(a, b, c):
    #setr (set register) copies the contents of register A into register C. (Input B is ignored.)
    #registers[c] = registers[a]
    print 'set', registers[a], registers[c]

def seti(a, b, c):
    #seti (set immediate) stores value A into register C. (Input B is ignored.)
    #registers[c] = a
    print 'set', a, registers[c]

#Greater-than testing:
def gtir(a, b, c):
    #gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
    #registers[c] = 1 if a > registers[b] else 0
    print 'gt', a, registers[b], registers[c]

def gtri(a, b, c):
    #gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
    #registers[c] = 1 if registers[a] > b else 0
    print 'gt', registers[a], b, registers[c]

def gtrr(a, b, c):
    #gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.
    #registers[c] = 1 if registers[a] > registers[b] else 0
    print 'gt', registers[a], registers[b], registers[c] 

#Equality testing:
def eqir(a, b, c):
    #eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
    #registers[c] = 1 if a == registers[b] else 0
    print 'eq', a, registers[b], registers[c]

def eqri(a, b, c):
    #eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
    #registers[c] = 1 if registers[a] == b else 0
    print 'eq', registers[a], b, registers[c]

def eqrr(a, b, c):
    #eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.
    #registers[c] = 1 if registers[a] == registers[b] else 0
    print 'eq', registers[a], registers[b], registers[c]

opcodes = {
    'addr': addr,
    'addi': addi,
    'mulr': mulr,
    'muli': muli,
    'banr': banr,
    'bani': bani,
    'borr': borr,
    'bori': bori,
    'setr': setr,
    'seti': seti,
    'gtir': gtir,
    'gtri': gtri,
    'gtrr': gtrr,
    'eqir': eqir,
    'eqri': eqri,
    'eqrr': eqrr
}


# seti 5 0 1

# now run the instructions
registers = list('abcdef')
for line in instructions:

    codes = line.split(' ')
    opname = codes[0]
    a, b, c = [int(x) for x in codes[1:]]
    operator = opcodes[opname]
    operator(a, b, c)


'''
add c 16 c
set 1 d
set 1 b
mul d b f
eq f e f
add f c c
add c 1 c
add d a a
add b 1 b
gt b e f
add c f c
set 2 c
add d 1 d
gt d e f
add f c c
set 1 c
mul c c c
add e 2 e
mul e e e
mul c e e
mul e 11 e
add f 7 f
mul f c f
add f 4 f
add e f e
add c a c
set 0 c
set c f
mul f c f
add c f f
mul c f f
mul f 14 f
mul f c f
add e f e
set 0 a
set 0 c
'''