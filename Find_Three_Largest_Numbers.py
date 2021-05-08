def findThreeLargestNumbers(array):
    newArray = list(reversed(sorted(array)))
    return [newArray[2], newArray[1], newArray[0]]
