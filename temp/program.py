def minimumCharactersForWords(words):
    # Write your code here.
    result = {}
    for word in words:
        frequencyForWord = getFrequency(word)
        updateCurrentResult(result, frequencyForWord)
    resultList = showFrequency(result)
    return resultList


def getFrequency(word):
    tempResult = {}
    for char in word:
        if char in tempResult:
            tempResult[char] += 1
        else:
            tempResult[char] = 1
    return tempResult


def updateCurrentResult(result, frequencyForWord):
    for key in frequencyForWord:
        frequency = frequencyForWord[key]
        if key in result:
            result[key] = max(frequency, result[key])
        else:
            result[key] = frequency


def showFrequency(result):
    templist = []
    for key in result:
        frequency = result[key]
        while frequency > 0:
            templist.append(str(key))
    return templist
