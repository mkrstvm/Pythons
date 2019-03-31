import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
#def formingMagicSquare(s):

s = input()
a = set()
b = 0
while 1:
    d = 0
    
    d = sum( int(x) ** 2 for x in s)

    if(d == 1):
        print("true")
        break
    if(d in a):
        print("false")
        break
    a.add(d)
    s = str(d)