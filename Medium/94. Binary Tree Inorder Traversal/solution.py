# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
inorder : left self right
preorder : self left right
postorder : left right self
"""

# Use recursive solution
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        self.traverse(root, ret)
        return ret
    
    def traverse(self, node, ret):
        if node is None:
            return
        self.traverse(node.left, ret)
        ret.append(node.val)
        self.traverse(node.right, ret)

