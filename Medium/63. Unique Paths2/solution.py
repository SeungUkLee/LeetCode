class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: 'List[List[int]]') -> 'int':
        row: int = len(obstacleGrid)
        col: int = len(obstacleGrid[0])
        dp: List[List[int]] = [[0] * col for _ in range(row)]
        dp[0][0] = 1
        
        for i in range(0, row):
            for j in range(0, col):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] += dp[i-1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j-1]
        return dp[row-1][col-1]


