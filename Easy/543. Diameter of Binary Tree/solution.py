# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        self.dfs(root)
        return self.ans
    
    def dfs(self, node):
        if not node:
            return 0

        left, right = self.dfs(node.left), self.dfs(node.right)
        self.ans = max(self.ans , left + right)
            
        return max(left, right) + 1

