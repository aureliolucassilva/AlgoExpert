def productSum(array, multiplier=1):
    totalSum = 0
    for element in array:
        if hasattr(element, '__len__'):
            totalSum = totalSum + multiplier * productSum(element, multiplier + 1)
        else:
            totalSum = totalSum + element * multiplier
    return totalSum
