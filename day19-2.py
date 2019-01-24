# 18200448
#
# https://adventofcode.com/2018/day/19

def getResult(a, b, c, d, e, f):
    a = 0
    for d in range(1, e + 1):
        if e % d == 0: # it's divisible
            a += d

    return a


# part 1, starting with a = 2
a, b, c, d, e, f = 0, 0, 1, 0, 994, 158
d = 1
print 'Part 1:', getResult(a, b, c, d, e, f)

# part 2, starting with a = 1
a, b, c, d, e, f = 0, 0, 0, 0, 10551394, 10550400
d = 1


print 'Part 2:', getResult(a,b,c,d,e,f)



'''
for d in range 1 to e
    for b in range 1 to e
        how many times does b * d == f
        add up all the d's where that happens
'''

'''
for d in range(1, e + 1):
    for b in range(1, e + 1):
        if d * b == e:
            a += d
            print 'f == e', a, b, c, d, e, f
    print a, b, c, d, e, f
'''

'''
a, b, c, d, e, f = 0, 0, 1, 0, 994, 158
d = 1

while d <= e:
    b = 1
    while b <= e:
        # this loop will run e times
        f = d * b
        if f == e:      # this can only happen if e == d
            a += d
            print 'f == e', a, b, c, d, e, f
        b += 1
    print a, b, c, d, e, f
    d += 1

'''

'''
2  set 1 b         # b = 1         -> LOOP FROM 25                             while d <= e                                        
3  mul d b f       # f = d * b     -> LOOP FROM from 11                            while b <= e
4  eq f e f        # f = 1 if f == e else 0   note that e > f                          if f == e: 
5  add f c c       # c = c + f     -> skip next if e == f                                  a += d
6  add c 1 c       # c += 1        -> skip next
7  add d a a       # a = a + d     -> a increments by d each time e == f *********
8  add b 1 b       # b = b + 1     -> go here in either case                           b += 1
9  gt b e f        # f = 1 if b > e else 0             
10 add c f c       # c = c + f     -> skip next if b > e                           
11 set 2 c         # c = 2         -> LOOP back to 3
12 add d 1 d       # d += 1        -> go here if b > e                             d += 1
13 gt d e f        # f = 1 if d > e else 0                                         if d > 3: exit
14 add f c c       # c = c + f     -> PROGRAM EXIT, if d > e
15 set 1 c         # c = 1         -> LOOP back to 2
16 mul c c c       # c = c * c     -> PROGRAM EXIT


'''

