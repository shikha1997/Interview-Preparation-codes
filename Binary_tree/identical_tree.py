class Node:
    def __init__(self,data):
        self.data = data
        self.left=None
        self.right=None

def identical(rootA,rootB):
    if(rootA is None and rootB is None):
        return True
    if(rootB and rootA):
        return rootB.data==rootA.data and identical(rootA.left,rootB.left) and identical(rootA.right,rootB.right)
    return False


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    root1 = None
    # root1.left = Node(2)
    # root1.right = Node(3)
    # root1.left.left = Node(4)
    # root1.left.right = Node(5)

    print(identical(root,root1))