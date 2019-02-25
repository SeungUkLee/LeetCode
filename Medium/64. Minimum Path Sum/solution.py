class Solution:
    def minPathSum(self, grid: 'List[List[int]]') -> 'int':
        grid_row_len: int = len(grid)
        grid_col_len: int = len(grid[0])
        dp: List[List[int]] = [[0] * grid_col_len] * grid_row_len
        dp[0][0] = grid[0][0]
        
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if i == 0 and j == 0:
                    continue    
                up: int = dp[i-1][j] if i > 0 else None
                left: int = dp[i][j-1] if j > 0 else None
                dp[i][j]: int = self.minimizes_sum(up, left) + grid[i][j]
        
        return dp[-1][-1]
    
    def minimizes_sum(self, x, y):
        if x is None:
            return y
        if y is None:
            return x
        return min(x, y)

