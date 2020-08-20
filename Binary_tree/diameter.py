class Node:
    def __init__(self,data):
        self.data = data
        self.left=None
        self.right=None

def height(root):
    if(root is None):
        return 0

    return max(height(root.left),height(root.right))+1

def diameter(root):
    if root is None:
        return 0
    l_height=height(root.left)
    r_height = height(root.right)

    l_diameter = diameter(root.left)
    r_diameter = diameter(root.right)

    return max(l_height+r_height+1,max(l_diameter,r_diameter))

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(diameter(root))