#!/usr/bin/env python3

# Helper program to compute the dissonance value of a triad or tetrad.
# Also outputs all possible inversions of the chord
# Example:  Input: ./tetrads.py 3 4 5
#          Output: +3+7|+4+9|+5+8|0.2833333333333333


import sys

r = [0.0,1.0,0.7,0.4,0.35,0.1,0.7,0.1,0.35,0.4,0.7,1.0,0.0]

def tetrad(a,b,c,d):
    x = r[a]+r[b]+r[c]+r[d]
    x += r[a+b]+r[b+c]+r[c+d]+r[d+a]
    x += r[a+b+c]+r[b+c+d]+r[c+d+a]+r[d+a+b]
    x /= 12.0
    print("+{}+{}+{}|+{}+{}+{}|+{}+{}+{}|+{}+{}+{}|{}".format(a,a+b,a+b+c,b,b+c,b+c+d,c,c+d,c+d+a,d,d+a,d+a+b,x))
    
def triad(a,b,c):
    x = r[a]+r[b]+r[c]
    x += r[a+b]+r[b+c]+r[c+a]
    x /= 6.0
    print("+{}+{}|+{}+{}|+{}+{}|{}".format(a,a+b,b,b+c,c,c+a,x))
    
if len(sys.argv) == 4:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
    triad(a,b,c)

elif len(sys.argv) == 5:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
    d = int(sys.argv[4])
    tetrad(a,b,c,d)

elif len(sys.argv) >= 2 and (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
    print("Support either 3 or 4 between intervals of chords to generate the dissonance and all inversions")
else:
    print("Wrong count of arguments")
