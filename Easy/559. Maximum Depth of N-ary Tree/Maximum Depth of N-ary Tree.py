# My Solution 

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
## use BFS
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        
        q = list()
        q.append(root)
        depth = 0
        while q:
            depth += 1
            size = len(q)
            for _ in range(size):
                node = q.pop(0)
                for child in node.children:
                    q.append(child)
        return depth

# Another Solution
## use recursion
class Solution(object):
    def maxDepth(self, root):
        if not root: return 0
        if not root.children: return 1
        return max(self.maxDepth(node) for node in root.children) + 1

## use BFS
class Solution(object):
    def maxDepth(self, root):
        q, level = root and [root], 0
        while q:
            q, level = [child for node in q for child in node.children if child], level + 1
        return level 

## use DFS
class Solution(object):
    def maxDepth(self, root, level = 1):
        return max(root and [self.maxDepth(child, level + 1) for child in root.children] + [level] or [0])