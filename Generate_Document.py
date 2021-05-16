def generateDocument(characters, document):
    hashChar = {}
    for element in characters:
        if element in hashChar.keys():
            hashChar[element] += 1
        else:
            hashChar[element] = 1
    for element in document:
        if element in hashChar.keys():
            hashChar[element] -= 1
        else:
            return False
    writeDocument = -1 not in hashChar.values()
    return writeDocument
