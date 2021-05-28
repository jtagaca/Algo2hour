
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


# def maximumToys(prices, k):
#     # Write your code here
#     # we can sort or pop it min then minus the k then plus the count but that might be
#     counter = 0
#     pricesRef = prices.copy()

#     for i in range(len(prices)):
#         if prices[i] > k:
#             continue
#         else:

#             # //TODO  15 minutes to debug if not then just do the transform method
#             # for i in range
#             h = min(pricesRef)
#             if k > 0 and k-h < k:

#                 k = k - h
#                 pricesRef.remove(h)
#                 counter += 1
#             # print(pricesRef)
#     return counter

# On(logn) in tbecauseweareusingatransfromalgorithmthatwilltransformthearray
# and the space is O(1) because there was not a need for extra memory

def maximumToys(prices, k):
    prices.sort()
    counter = 0
    for i in range(len(prices)):
        if prices[i] <= k:
            k = k-prices[i]
            counter += 1

    return counter


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
