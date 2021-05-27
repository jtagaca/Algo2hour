def minimumSwaps(arr):

    # time complexity = O(n) and space is O(1) because there is no wasted space, in worst case scenario
    # where all the items are unordered and you have to swap each of them
    # this will run 2n because of while loop not needing to run for each iteration in the for loop
    # so O(n) in big O
    counter = 0
    for i in range(0, len(arr)):
        value = i + 1
        # while 1 is not equal to 1 run this loop
        # value is the proper value that should be on that index
        # example at index 0 it should be the number 1
        #
        while value != arr[i]:
            # we find the swapIndex through getting the value of arr at index i which is 4-1 =3
            # so index is 3
            swapIndex = arr[i] - 1
            # currenVal = arr[i]
            # swapValue =
            # we swap with the current value and the swapvalue at index of swapindex
            arr[i], arr[swapIndex] = arr[swapIndex], arr[i]
            counter += 1

    return counter


arr = [4, 3, 1, 2]

v = minimumSwaps(arr)
