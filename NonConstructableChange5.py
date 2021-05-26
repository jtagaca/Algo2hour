# O(n) S-O(1) if you don't know how to solve the problem try and transform it and see if there is a pattern
def nonConstructibleChange(coins):
    coins.sort()
    change = 0
    if len(coins) == 0:
        return 1
    else:
        for coin in coins:

            if coin > change+1:
                break
            else:
                change += coin
    return change+1

    # Write your code here.
