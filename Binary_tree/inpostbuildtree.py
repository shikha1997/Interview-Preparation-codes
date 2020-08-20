class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def buildTree(inorder,postorder,beg,end,mp):

    if(beg>end):
        return None
    t = Node(postorder[buildTree.postIndex])
    inIndex = mp[postorder[buildTree.postIndex]]
    buildTree.postIndex-=1

    if(beg==end):
        return t

    t.right = buildTree(inorder,postorder,inIndex+1,end,mp)
    t.left = buildTree(inorder, postorder, beg, inIndex - 1, mp)

    return t


def printInorder(node):
    if node is None:
        return
    printInorder(node.left)
    print(node.data,end=" ")
    printInorder(node.right)


if __name__ == '__main__':
    In = [4, 8, 2, 5, 1, 6, 3, 7]
    post = [8, 4, 5, 2, 6, 7, 3, 1]
    # Static variable preIndex
    mp=dict()
    for i in range(len(In)):
        mp[In[i]]=i

    buildTree.postIndex = len(post)-1
    root = buildTree(In, post, 0, len(In) - 1,mp)
    printInorder(root)
    print()