class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # hashmap 이용
        dic_nums = {}
        
        for i, num in enumerate(nums):
            check_num = target - num
            if check_num in dic_nums:
                return [dic_nums[check_num], i]
            dic_nums[num] = i
        return None