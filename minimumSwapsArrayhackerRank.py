def minimumSwaps(arr):

    # time complexity = O(n) and space is O(1) because there is no wasted space, in worst case scenario
    # where all the items are unordered and you have to swap each of them

    counter = 0
    for i in range(0, len(arr)):
        value = i + 1
        # while 1 is not equal to 1 run this loop
        while value != arr[i]:
            swapIndex = arr[i] - 1
            # currenVal = arr[i]
            # swapValue =
            arr[i], arr[swapIndex] = arr[swapIndex], arr[i]
            counter += 1

    return counter


arr = [4, 3, 1, 2]

v = minimumSwaps(arr)
