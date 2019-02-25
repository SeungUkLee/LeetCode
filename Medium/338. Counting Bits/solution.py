class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0] * (num + 1)
        sq = 1
        for i in range(1, num + 1):
            if i < sq:
                res[i] = res[i - sq//2] + 1
            else:
                res[i] = res[i - sq] + 1 
                sq *= 2
        return res