def insertionSort(array):
    for idx in range(1, len(array)):
        innerIdx = idx - 1
        while innerIdx >= 0:
            if array[idx] < array[innerIdx]:
                oldNum = array[idx]
                array[idx] = array[innerIdx]
                array[innerIdx] = oldNum
                idx -= 1
            innerIdx -= 1
    return array
