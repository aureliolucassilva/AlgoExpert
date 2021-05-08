def bubbleSort(array, offset=1):
    swap = False
    for idx in range(len(array) - offset):
        if array[idx] > array[idx + 1]:
            oldNumber = array[idx]
            array[idx] = array[idx + 1]
            array[idx + 1] = oldNumber
            swap = True
    if swap:
        offset = offset + 1
        bubbleSort(array, offset)

    return array
