#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#


def makeAnagram(a, b):
    # Wr
    # ite your code here
    inWord = {}
    # Time complexity = O(n) and space complexity = O(n)
    # what did they do here is that
    # we create a dictionary for thefirststring and
    # use a -1 to keep removing the occurences of the value in string b
    # if they are 0 then it means that it has the same occurences in string a and string b
    # if not then it means that there maybe an extra one in string b or string a

    inWord = Counter(a)
    for value in b:
        inWord[value] -= 1

    value = inWord.values()
    total = sum(abs(i) for i in value)
    # print(inWord)
    return total


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    # fptr.write(str(res) + '\n')

    # fptr.close()
