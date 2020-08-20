class Node:
    def __init__(self,data):
        self.data = data
        self.left=None
        self.right=None

def inorder_trav(root):
    # if(root is None):
    #     return
    if(root):
        inorder_trav(root.left)
        print(root.data,end=" ")
        inorder_trav(root.right)

def inorder_recursion(root):
    # if(root is None):
    #     return
    stk=[]
    curr=root
    while(1):
        if(curr is not None):
            stk.append(curr)
            curr=curr.left
        elif(len(stk)):
            curr=stk.pop()
            print(curr.data,end=" ")
            curr=curr.right
        else:
            break



if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    inorder_trav(None)
    inorder_recursion(root)
    print()

