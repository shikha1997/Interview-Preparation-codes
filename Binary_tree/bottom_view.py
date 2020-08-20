#Top View of Binary Tree
class Node:
    def __init__(self,data):
        self.data = data
        self.left=None
        self.right=None
        self.hd = 0


def bottom_view(root):
    if (root == None):
        return
    q = []
    m = dict()
    hd = 0
    root.hd = hd
    q.append(root)
    while(len(q)):
        root = q[0]
        hd = root.hd
        #if hd not in m:
        m[hd] = root.data
        if (root.left):
            root.left.hd = hd - 1
            q.append(root.left)

        if (root.right):
            root.right.hd = hd + 1
            q.append(root.right)

        q.pop(0)
    for i in sorted(m):
        print(m[i], end=" ")

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    bottom_view(root)
    print()



