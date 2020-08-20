#Check if Binary tree is height balanced or not
class Node:
    def __init__(self,data):
        self.data = data
        self.left=None
        self.right=None

def height(root):
    if(root is None):
        return 0

    return max(height(root.left),height(root.right))+1

def ch_bal(root):
    if root is None:
        return False
    lh=height(root.left)
    rh=height(root.right)
    if(abs(lh-rh)==1 or lh==rh):
        return True
    return False

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.left.left = Node(5)


    print(ch_bal(root))