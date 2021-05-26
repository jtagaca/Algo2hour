
this has a t of O(N) because we iterated over the whole array it can be max of 3(n) and the space complexity isO(1) because it uses in place and the size does not grow


def longestPeak(array):
    i = 1
    highestLength = 0
    while i < len(array)-1:
        current = i
        prev = i-1
        nxt = i+1
        isPeak = array[current] > array[prev] and array[current] > array[nxt]
        if not isPeak:
            i += 1
            continue
        left = prev
        prevleft = left-1
        while prevleft >= 0 and array[left] > array[prevleft]:
            left -= 1
            prevleft = left-1
        right = nxt
        nextRight = right+1
        while nextRight < len(array) and array[right] > array[nextRight]:
            right += 1
            nextRight = right+1
        currentLength = (nextRight-prevleft-1)
        highestLength = max(currentLength, highestLength)
        i += 1

    return highestLength


array = [1, 2, 3, 4, 5, 1]
gg = longestPeak(array)
print(gg)

# we keep checking if it's till a peak if the prev is less than or more than
# stop chceking once
# keep track of the direction as well so a boolean
# How to implement unit testing in vscode with hacker rank questions
