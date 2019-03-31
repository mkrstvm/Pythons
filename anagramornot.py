import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
#def formingMagicSquare(s):

def anagram(s1,s2):
    if( len(s1) != len(s2)):
        print("false")
        return
    for x in range(len(s2)):
        if(s1[x] != s2[x]):
            print("false")
            return
    print("true")

s1 = input()
s1 = list(s1)

s2 = input()
s2 = list(s2)

s1.sort()
s2.sort()
anagram(s1,s2)


