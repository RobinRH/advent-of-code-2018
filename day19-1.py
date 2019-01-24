# 1728
# takes a while to run
# https://adventofcode.com/2018/day/19

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
#print(iRegister)

# seti 5 0 1
instructions = lines[1:]
#print instructions

registers = [0,0,0,0,0,0]

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
registers = [0] * 6
iptr = registers[iRegister]
while iptr >= 0 and iptr < len(instructions):
    # write iptr to the iregister
    registers[iRegister] = iptr
    #if iptr == 1: print registers
    codes = instructions[iptr].split(' ')
    opname = codes[0]
    a, b, c = [int(x) for x in codes[1:]]
    operator = opcodes[opname]
    operator(a, b, c)
    # read back the iptr
    iptr = registers[iRegister]
    # increment it
    iptr += 1

print registers[0]
