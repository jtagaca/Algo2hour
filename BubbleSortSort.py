#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#


def countSwaps(a):
    # Write your code here
    # we are bubling the current element to the last and after getting him to the lase position then we run the loop again
    # Time complexity = O(n^2) and Space is O(1)
    count = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            print(j)
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                count += 1
    print("Array is sorted in %d swaps." % count)
    print("First Element: %d" % a[0])
    print("Last Element: %d" % a[-1])


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
