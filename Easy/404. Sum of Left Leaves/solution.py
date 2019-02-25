# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: 'TreeNode') -> 'int':
        return self.recur(root, False)
    
    def recur(self, root, is_left):
        if root is None:
            return 0
        if is_left and root.left is None and root.right is None:
            return root.val
        return self.recur(root.left, True) + self.recur(root.right, False)