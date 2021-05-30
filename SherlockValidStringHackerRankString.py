#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


# TimeComplexity is O(n) and spacecomplexity is O(1)
# create two dictionary that you will use to keep track of the frequency
# we find the min and max of the frequency
# we have a test case where if the len of frequency is 1 then it means that the
# a letter is repeated the same times

def isValid(s):
    c = Counter(s)
    freq = Counter(c.values())
    if len(freq) == 1 and freq.values() == 1:
        return "YES"
    elif len(freq) == 2:
        key_max = max(freq.keys())
        key_min = min(freq.keys())
        if key_max - key_min == 1 and freq[key_max] == 1:
            return "YES"
        elif key_min == 1 and freq[key_min] == 1:
            return "YES"
    return "NO"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)
    print(result)
    # fptr.write(result + '\n')

    # fptr.close()
