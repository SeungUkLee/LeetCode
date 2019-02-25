# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    root is None return 0
    root.val < L : 오른쪽 서브트리만 탐색
    root.val > R : 왼쪽 서브트리만 탐색
    L <= root.val <= R: 왼쪽 서브트리 + 자신값 + 오른쪽 서브트리
    """
    def rangeSumBST(self, root: 'TreeNode', L: 'int', R: 'int') -> 'int':
        if root is None:
            return 0
        elif root.val < L:
            return self.rangeSumBST(root.right, L, R)
        elif root.val > R:
            return self.rangeSumBST(root.left, L, R)
        else:
            return self.rangeSumBST(root.left, L, R) + root.val + self.rangeSumBST(root.right, L, R)