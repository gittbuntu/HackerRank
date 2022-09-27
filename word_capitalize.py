import math
import os
import random
import re
import sys

new_string = []


def solve(s):
    string = s.split(" ")
    for i in string:
        new_string.append(i.capitalize())
    final_string = " ".join(new_string)
    return final_string


# fptr = open(os.environ['OUTPUT_PATH'], 'w')
with open('F:\HackerRank\string.txt', 'a') as fptr:
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
