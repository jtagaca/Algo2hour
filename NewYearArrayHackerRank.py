import sys
import re
import random
import os
import math

#!/bin/python3


#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    count = 0
    for i in reversed(range(len(q))):
        if q[i] != i + 1:
            if q[i - 1] == i + 1:
                count += 1
                q[i], q[i - 1] = q[i - 1], q[i]
            elif q[i - 2] == i + 1:
                count += 2
                q[i-2], q[i - 1] = q[i - 1], q[i-2]
                q[i], q[i - 1] = q[i - 1], q[i]

            else:
                print("chaotic")
                break
    print(count)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
