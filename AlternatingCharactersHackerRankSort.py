#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


# O(n) for time complexity and O(1) for space complexity
# we try and check to see if the left is not equal to the right and if they are not then we just skip it but if they are then we have 
# to increase the delete count
def alternatingCharacters(s):
    # Write your code here
    deleted =0
    for i in range(1,len(s)):
        left= i-1
        right = i
        if s[left]!=s[right]:
            continue
        else:
            deleted+=1  
    return deleted
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
