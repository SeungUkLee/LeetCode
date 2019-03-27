# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        # cur, stack, inorder = root, [], float('-inf')
        cur, stack, inorder = root, [], None
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            
            # if cur.val <= inorder:
            if inorder is not None and cur.val <= inorder:
                return False
            inorder = cur.val
            cur = cur.right
            
        return True

