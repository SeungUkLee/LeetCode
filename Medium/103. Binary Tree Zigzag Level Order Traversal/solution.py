# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        deq = [root]
        res = []
        flag = 1 # if 1 is 'left to right'
        
        while deq:
            level_nodes = []
            size = len(deq)
            for _ in range(size):
                node = deq.pop(0)
                level_nodes.append(node.val)

                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
            if flag == -1:
                level_nodes.reverse()    
            res.append(level_nodes)
            flag *= -1
        return res
        