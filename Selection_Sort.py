def selectionSort(array, start=0):
    # Start of unsorted array
    smallest = array[start]
    smallIdx = start
    # Comparision
    for idx in range(start, len(array)):
        if smallest > array[idx]:
            smallest = array[idx]
            smallIdx = idx
    oldNum = array[start]
    array[start] = smallest
    array[smallIdx] = oldNum
    # Recursion
    if start < len(array) - 1:
        selectionSort(array, start + 1)
    return array
