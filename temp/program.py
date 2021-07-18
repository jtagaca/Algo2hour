def hasSingleCycle(array):
    # Write your code here.
    elementsVisited = 0
    currentIdx = 0
    while elementsVisited < len(array):
        if elementsVisited > 0 and currentIdx == 0:
            return False
        elementsVisited += 1
        currentIdx = getJump(array, currentIdx)
    return currentIdx == 0s


def getJump(array, currentIdx):
    jump = array[currentIdx]
    nextIdx = (currentIdx+jump) % len(array)
    return nextIdx if nextIdx >= 0 else nextIdx+len(array)
