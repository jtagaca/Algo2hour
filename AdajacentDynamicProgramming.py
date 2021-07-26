def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]
    second = array[0]
    first = max(array[0], array[1])
    # first will contain the element that has the highest value and the second will contain
    # the value that can be summed up with the current position of the array or i at this case.
    # and the trick is that it does not need to  be i-1 or i-2 but rather the first will always contain
    # the highest that we can sum up and the second will contain value that we can use to either sum with the current position
    for i in range(2, len(array)):
        current = max(first, second + array[i])
        second = first
        first = current
    return first
