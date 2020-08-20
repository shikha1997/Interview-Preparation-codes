class Node:
    def __init__(self,data):
        self.data = data
        self.left=None
        self.right=None

def postorder_trav(root):
    # if(root is None):
    #     return
    if(root):
       # print(root.data, end=" ")
        postorder_trav(root.left)
        postorder_trav(root.right)
        print(root.data, end=" ")


def postorder_recursion(root):
    if(root is None):
        return


    curr=root
    visited = set()
    while (curr and curr not in visited):
        if (curr.left and curr.left not in visited):
            curr=curr.left
        elif (curr.right and curr.right not in visited):
            curr = curr.right
        else:
            print(curr.data,end=" ")
            visited.add(curr)
            curr=root




if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
   # postorder_trav(root)
    postorder_recursion(root)
    print()

