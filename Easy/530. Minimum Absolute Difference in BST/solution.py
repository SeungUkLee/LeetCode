# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # Binaray Search Tree 성질 : inorder -> 오름차순 정렬이 됨!
    def getMinimumDifference(self, root: 'TreeNode') -> 'int':
        inorder_list = []
        self.inorder(root, inorder_list)
        return min(abs(a - b) for a, b in zip(inorder_list, inorder_list[1:]))
    
    def inorder(self, root, l):
        if root.left:
            self.inorder(root.left, l)
        l.append(root.val)
        if root.right:
            self.inorder(root.right, l)
    