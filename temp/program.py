def searchForRange(array, target):
    # Write your code here.
    finalRange = [-1, -1]

    getFinalRange(array, target, 0, len(array)-1, finalRange, True)
    getFinalRange(array, target, 0, len(array)-1, finalRange, False)

    return finalRange


def getFinalRange(array, target, l, r, finalRange, goLeft):

    while l <= r:
        mid = (l+r)//2
        currentNum = array[mid]

        if target < currentNum:
            r = mid-1
        elif target > currentNum:
            l = mid+1
        else:
            if goLeft:
                if array[mid-1] != target or mid == 0:
                    finalRange[0] = mid
                else:
                    r = mid-1
            else:
                if array[mid+1] != target or mid == len(array)-1:
                    finalRange[1] = mid
                else:
                    l = mid+1
