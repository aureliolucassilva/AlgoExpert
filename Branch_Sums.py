class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def depthFirstSearch(node, sumNode, sumArray):
    # Node == None
    if node is None:
        return
    # Sum
    sumNode = sumNode + node.value
    # Leaf Node
    if node.left is None and node.right is None:
        sumArray.append(sumNode)
        return sumArray
    # Recursion
    depthFirstSearch(node.left, sumNode, sumArray)
    depthFirstSearch(node.right, sumNode, sumArray)


def branchSums(root):
    sumNodes = []
    depthFirstSearch(root, 0, sumNodes)
    return sumNodes
