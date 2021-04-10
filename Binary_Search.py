def binarySearch(array, target):
    leftPointer = 0
    rightPointer = len(array) - 1

    while leftPointer <= rightPointer:
        middlePointer = (leftPointer + rightPointer) // 2
        if array[middlePointer] > target:
            rightPointer = middlePointer - 1
        elif array[middlePointer] < target:
            leftPointer = middlePointer + 1
        elif array[middlePointer] == target:
            return middlePointer
    
    return -1
