#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#


# we are removing the first element then appending it to the last index
# this will run O(1) space because we are not using extra memory or change the length of the given array
# one thing that we can do if optimization is required is that we can slice the array into two parts and return that array
def rotLeft(a, d):
    # O(n)T  O(1)S
    # Write your code here
    for i in range(d):
        v = a.pop(0)
        a.append(v)
    return a


# split the array into two sub arrays and re joined them together after getting split
# first array is the index that is getting split so starting from index (d) to end then we make another sub array that is
# from the start to the index not including d

# this has a time complexity of O(1) and space complexity of O(1)
def rotLeft(a, d):
    # O(n)T  O(1)S
    # Write your code here
    a = a[d:]+a[:d]
    return a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
