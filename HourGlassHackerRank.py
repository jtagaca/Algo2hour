#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

# we can only traverse the array 4 times because of the middle point when you pin point the middle point by row or column the bounds will show
# time complexity is O(N^2) and space complexity is O(1)


def hourglassSum(arr):
    # Write your code here
    # we need to have a tracker of the highest

    maxnum = -63
    for row in range(4):
        for col in range(4):
            top = sum(arr[row][col: col + 3])
            middle = arr[row + 1] + arr[col + 1]
            bottom = sum(arr[row + 2][col:col+3])

            currenttotal = top+middle+bottom
            maxnum = max(currenttotal, maxnum)
    return maxnum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
