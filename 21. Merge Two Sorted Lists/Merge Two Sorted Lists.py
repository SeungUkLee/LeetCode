"""
My Solution
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = None
        cur = None
        while l1 != None or l2 != None:
            if l2 == None or (l1 != None and l1.val < l2.val):
                if ret == None:
                    ret = l1
                    cur = l1
                    l1 = l1.next
                else:
                    cur.next = l1
                    cur = l1
                    l1 = l1.next
            else:
                if ret == None:
                    ret = l2
                    cur = l2
                    l2 = l2.next
                else:
                    cur.next = l2
                    cur = l2
                    l2 = l2.next
        return ret

Ref = "https://leetcode.com/problems/merge-two-sorted-lists/discuss/9735/Python-solutions-(iteratively-recursively-iteratively-in-place)."