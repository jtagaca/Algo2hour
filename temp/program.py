phoneLookUp = {
    "0": ["0"],
    "1": ["1"],
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}


def phoneNumberMnemonics(phoneNumber):
    # time complexity is O(4^n* N) where 4 is the maximum len of a digit in the digit hash map an d the
    # n is the len of a input digit where N is the time it takes to create a list or concatinate it so we do it every time we
    # hit the base case
    # Write your code here.
    currentMne = ["0"]*len(phoneNumber)
    result = []
    helperMne(0, currentMne, phoneNumber, result)
    return result


def helperMne(idx, currentMne, phoneNumber, result):
    if idx == len(phoneNumber):
        # we are checking for extra call and if so then we can append.
        # we make a string out of a list
        currentString = ''.join(currentMne)
        result.append(currentString)
    else:
        # we recursively call the value to the current mne for every letter.
        digit = phoneNumber[idx]
        # we use idx to keep track of the digit that we are in and
        # the recursion call
        values = phoneLookUp[digit]
        for value in values:
            currentMne[idx] = value
            helperMne(idx+1, currentMne, phoneNumber, result)
