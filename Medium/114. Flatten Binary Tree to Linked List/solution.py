# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        pre_v = root
        for v in self.preorder(root):
            if v is pre_v:
                continue
            pre_v.left = None
            pre_v.right = v
            pre_v = v
    
    def preorder(self, root):
        if not root:
            return None
        left, right = root.left, root.right
        yield root
        yield from self.preorder(left)
        yield from self.preorder(right)