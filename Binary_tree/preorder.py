class Node:
    def __init__(self,data):
        self.data = data
        self.left=None
        self.right=None

def preorder_trav(root):
    # if(root is None):
    #     return
    if(root):
        print(root.data, end=" ")
        preorder_trav(root.left)
        preorder_trav(root.right)


def preorder_recursion(root):
    if(root is None):
        return

    stk=[root]
    while(len(stk)):
        n=stk.pop()
        print(n.data,end=" ")
        if(n.right):
            stk.append(n.right)
        if(n.left):
            stk.append(n.left)



if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    #preorder_trav(root)
    preorder_recursion(root)
    print()

