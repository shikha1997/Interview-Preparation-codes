class Node:
    def __init__(self,data):
        self.data = data
        self.left=None
        self.right=None

def left_view(root,m,level):
    if(root is None):
        return
    if(m[0] < level):
        print(root.data,end=" ")
        m[0]=level
    left_view(root.left,m,level+1)
    left_view(root.right,m,level+1)


def left_view_main(root):
    m=[0]
    return left_view(root,m,1)

if __name__ == '__main__':
    # root = Node(1)
    # root.left = Node(2)
    # root.right = Node(3)
    # root.left.left = Node(4)
    # root.left.right = Node(5)
    root = Node(12)
    root.left = Node(10)
    root.right = Node(20)
    root.right.left = Node(25)
    root.right.right = Node(40)

    left_view_main(root)

    #Tc-o(n)