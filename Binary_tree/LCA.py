#LCA in Binary Tree
class Node:
    def __init__(self,data):
        self.data = data
        self.left=None
        self.right=None

def height(root):
    if(root is None):
        return 0

    return max(height(root.left),height(root.right))+1

def LCA(root,a,b):
    if(root is None):
        return
    if(root.data==a or root.data==b):
        return root
    l=LCA(root.left,a,b)
    r=LCA(root.right,a,b)
    if l and r:
        return root
    return l if l else r

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(LCA(root,5,3).data)