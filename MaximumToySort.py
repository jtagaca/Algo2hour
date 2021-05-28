
import math
import os
import random
import re
import sys

#
# Complete the 'maximumToys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER k
#


def maximumToys(prices, k):
    # Write your code here
    # we can sort or pop it min then minus the k then plus the count but that might be
    counter = 0
    pricesRef = prices.copy()s

    for i in range(len(prices)):
        if prices[i] > k:
            continue
        else:
            # for i in range
            g = pricesRef.pop(min(pricesRef))
            k = k - g
            counter += 1
    return counter


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()