# 14256686
#
# https://adventofcode.com/2018/day/21

a, b, c, d, e, f = 0,0,0,0,0,0

def printValues():
    print [a, b, c, d, e, f]

elist = [0]
diff = []
costs = []

def erecord():
    global ctr
    elist.append(e)
    if len(elist) == 10611: # by running the app, we know there are no more values of e after this one
        print e
        exit()        

def setup():
    global a, b, c, d, e, f

    f = d & 255           # f = 0 to 255 (select the rightmost 8 bits)
    e = e + f             # e = e + f
    e = 16777215 & e      # e = 0 to (256*256*256-1)   (rightmost 24 bits)
    e = e * 65899         # e = e * 65899          17 bits 0b10000000101101011
    e = 16777215 & e      # e = 0 to (256*256*256-1)    (rightmost 24 bits)
    #print e

ctr = 1
costs = {}
d = e | 65536         
e = 10552971          
setup()    # e = 14632729 , d = 65536
while True:
    d = d / 256    
    ctr += d * 256
    setup()
    if d < 256:
        erecord() # this is a halting value, the one to count and print out
        if a == e:
            exit()
        else:
            d = e | 65536    # if d drops below 256, then set the 256*256 bit,therefore d = e or d = e + 65536
            e = 10552971          
            setup()



'''
A helper app converts the input to this more readable opcode.
0  set 123 e           # e = 123
1  ban e 456 e         # e = 72
2  eq e 72 e           # e = 1
3  add e b b           # b = b + e (e is always 1)
4  set 0 b             # b = 0 (SKIPPED)
5  set 0 e             # e = 0
6  bor e 65536 d       # d = e | 65536 (sets the 65536 bit)    LOOP from 30     while a != e
7  set 10552971 e      # e = 10552971                                             d = e | 65546, e = 10552971
8  ban d 255 f         # f = d mod 256                 LOOP from 27               loop A 
9  add e f e           # e = f + 10552971                                               f = d mod 256, e = large, d > 65536
10 ban e 16777215 e    # e = e mod (256*256*256)                                        e < 16777216 (256*256*256)
11 mul e 65899 e       # e = e * 65899                                                  e is bigger
12 ban e 16777215 e    # e = e mod (256*256*256)                                        e < 16777216 (256*256*256)
13 gt 256 d f          # f = 1 if d <= 256 else 0                                       f = 0
14 add f b b           # b = b + f             SKIP to 16 if d <= 256                   if d <= 256 and a==e then EXIT
15 add b 1 b           # b += 1                SKIP to 17                            
16 set 27 b            # b = 27                SKIP to 28
17 set 0 f             # f = 0                                                          else f=0
18 add f 1 c           # c = f + 1 = 1         LOOP from 25                             while c < d (B)
19 mul c 256 c         # c = 256 * c                                                        c = f + 1
20 gt c d c            # c = 1 if c > d else 0                                              c *= 256
21 add c b b           # b = b + c             SKIP to 23 if c > d                       
22 add b 1 b           # b = b + 1             SKIP to 24 if c < d                          if c > d, then d = f and loop to 8
23 set 25 b            # b = 25                JUMP to 26 if c > d                          else f += 1 and loop to 18
24 add f 1 f           # f = f + 1                                                  
25 set 17 b            # b = 17                LOOP to 18                               loop (B)  
26 set f d             # d = f                 JUMP from 23                         
27 set 7 b             # b = 7                 LOOP to 8                          loop to A     (c > d)
28 eq e a f            # f = 1 if a == e else 0
29 add f b b           # b = f + b             EXIT if a==e
30 set 5 b             # b = 5                 LOOP to 6                        end while

if a == e, then e & 16777215 == a

'''