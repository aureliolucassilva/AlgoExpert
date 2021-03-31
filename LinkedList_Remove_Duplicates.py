class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList

    while currentNode is not None:
        currentNode = currentNode.next
        nextNode = currentNode.next

        while nextNode is not None and nextNode == currentNode:
            nextNode = nextNode.next

        currentNode.next = nextNode

    return linkedList
