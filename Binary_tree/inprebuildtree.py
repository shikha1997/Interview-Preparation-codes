class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def buildTree(inorder,preorder,beg,end,mp):

    if(beg>end):
        return
    t = Node(preorder[buildTree.preIndex])
    buildTree.preIndex+=1

    if(beg==end):
        return t
    inIndex=mp[preorder[buildTree.preIndex-1]]
    t.left=buildTree(inorder,preorder,beg,inIndex-1,mp)
    t.right=buildTree(inorder,preorder,inIndex+1,end,mp)

    return t


def printInorder(node):
    if node is None:
        return
    printInorder(node.left)
    print(node.data,end=" ")
    printInorder(node.right)


if __name__ == '__main__':
    inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
    preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
    # Static variable preIndex
    mp=dict()
    for i in range(len(inOrder)):
        mp[inOrder[i]]=i

    buildTree.preIndex = 0
    root = buildTree(inOrder, preOrder, 0, len(inOrder) - 1,mp)
    printInorder(root)
    print()