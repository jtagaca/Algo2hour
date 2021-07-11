def generateDocument(characters, document):
    # Write your code here.
    h = {"": float("inf")}
    for letter in characters:
        if letter in h:
            h[letter] += 1
        else:
            h[letter] = 1
    for letter in document:
        if letter in h:
            h[letter] -= 1
        else:
            return False
    return True
