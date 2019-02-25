# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: 'TreeNode') -> 'List[int]':
        if root is None:
            return []
        res, q = [], [root]
        while q:
            size = len(q)
            for i in range(size):
                cur = q.pop(0)
                if i == size - 1:
                    res.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return res
    
