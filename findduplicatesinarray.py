import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
#def formingMagicSquare(s):

def findduplicate(s1):
    a = []
    for x in range(len(s1)):
        if(s1[abs(s1[x])] < 0):
            a.append(abs(s1[x]))
        s1[abs(s1[x])] = -s1[abs(s1[x])]
    return a

s1 = input()
s1 = map(int,list(s1))
print(findduplicate(list(s1)))