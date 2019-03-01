class Solution:
    # Bucket Sort https://ratsgo.github.io/data%20structure&algorithm/2017/10/18/bucketsort/
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket, res = [[] for _ in range(len(nums) + 1)], []
        for num, frequency in collections.Counter(nums).items():
            bucket[frequency].append(num)
        
        for l in bucket[::-1]:
            if len(res) >= k:
                break
            if l:
                res += l
        return res