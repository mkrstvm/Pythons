import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
#def formingMagicSquare(s):

s = input()
s = s.replace(" ", "")
s = list(s)
n = len(s)
f = 0
l = n-1

while(f!=l):
    temp = s[f]
    s[f] = s[l]
    s[l] = temp
    f +=1
    l -=1

print("".join(str(x) for x in s))