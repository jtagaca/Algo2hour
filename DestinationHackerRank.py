
import math
import os
import random
import re
import sys


# def finalPosition(move):
#     l = len(move)
#     countUp, countDown = 0, 3
#     countLeft, countRight = 0, 1

#     for i in range(l):

#         if (move[i] == 'U'):
#             countUp += 1
#         elif(move[i] == 'D'):
#             countDown += 1
#         elif(move[i] == 'L'):
#             countLeft += 1
#         elif(move[i] == 'R'):
#             countRight += 1
#     return(countRight - countLeft), (countUp - countDown)


def getMaxDeletions(s):

    # destination = finalPosition(s)
    # return destination
    final = s
    Ucount = s.count("U")
    Dcount = s.count("D")
    lcount = s.count("L")
    rcount = s.count("R")
    del1count = 0
    del2count = 0
    maxDelcount = 0
    if Ucount > Dcount:
        del1count = Dcount
    else:
        del1count = Ucount
    if rcount > lcount:
        del2count = lcount
    else:
        del2count = rcount

    maxDelcount = del1count*2+del2count*2
    return maxDelcount


if __name__ == '__main__':

    s = input()
    result = getMaxDeletions(s)
    print(result)
