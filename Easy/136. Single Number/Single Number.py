"""
XOR 비트 연산자 사용.
두번 나오면 결국 그 비트는 0이 되므로 한번만 나온 비트만 1로 남아있다.
"""
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for n in nums:
            ret ^= n
        return ret