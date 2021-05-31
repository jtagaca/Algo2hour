import math
import os
import random
import re
import sys


def balancedSum(arr):
    # geting the len of the array for reuse
    lenArr = len(arr)
    # making a left sum array
    PreSum = [0] * lenArr
    PreSum[0] = arr[0]
    for i in range(1, lenArr):
        PreSum[i] = PreSum[i - 1] + arr[i]
    # making a right sum array
    CompareSum = [0] * lenArr
    CompareSum[lenArr - 1] = arr[lenArr - 1]
    # comparing from right to left of the left array and right array
    for i in range(lenArr - 2, -1, -1):
        CompareSum[i] = CompareSum[i + 1] + arr[i]
    for i in range(1, lenArr - 1, 1):
        if PreSum[i] == CompareSum[i]:
            return i
    return - 1


if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = []
    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)
    result = balancedSum(arr)
    print(result)
