def firstNonRepeatingCharacter(string):
    countChar = {}
    for element in string:
        if element in countChar.keys():
            countChar[element] += 1
        else:
            countChar[element] = 1
    for char, num in countChar.items():
        if num == 1:
            return string.index(char)

    return -1
