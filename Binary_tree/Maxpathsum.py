# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Leetcode probelm
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = -math.inf

        def mUtil(root):
            if (root is None):
                return 0
            l = mUtil(root.left)
            r = mUtil(root.right)

            self.res = max(self.res, l + r + root.val)
            return max(0, max(l, r) + root.val)

        mUtil(root)
        return self.res