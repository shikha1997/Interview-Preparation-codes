# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#RECURSIVE SOL
class Solution:
    def mirror(self, root1: TreeNode, root2: TreeNode) -> bool:
        if (root1 is None and root2 is None):
            return True
        if (root1 is None or root2 is None):
            return False
        return root1.val == root2.val and self.mirror(root1.left, root2.right) and self.mirror(root2.left, root1.right)

    def isSymmetric(self, root: TreeNode) -> bool:
        if (root is None):
            return True
        return self.mirror(root.left, root.right)

#ITERATIVE SOL
    def isSymmetric(self, root: TreeNode) -> bool:
        if root:
            q = []
            q.append(root)
            while len(q) > 0:
                tmp = []
                while len(q) > 0:
                    tmp.append(q.pop())
                n1 = []
                n2 = []
                for node in tmp:
                    if node.left:
                        n1.append(node.left.val)
                        q.append(node.left)
                    else:
                        n1.append("null")
                    if node.right:
                        n2.append(node.right.val)
                        q.append(node.right)
                    else:
                        n2.append("null")
                print(n1, n2)
                if n1 != n2[::-1]:
                    return False
            return True
        else:
            return True