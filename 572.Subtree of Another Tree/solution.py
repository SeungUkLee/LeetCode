# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: 'TreeNode', t: 'TreeNode') -> 'bool':
        if not s:
            return False
        if self.is_match(s, t):
            return True
        
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def is_match(self, s, t):
        if not (s and t):
            return s == t
        
        return s.val == t.val and self.is_match(s.left, t.left) and self.is_match(s.right, t.right)
