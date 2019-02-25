"""
My Solution
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        parentheses = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for c in s:
            if c in parentheses:
                stack.append(parentheses[c])
            else:
                pop_value = stack.pop() if stack else None
                if pop_value != c:
                    return False
        return True if not stack else False