# https://leetcode.com/problems/minimum-path-sum/?envType=study-plan-v2&envId=dynamic-programming
# 난이도: medium
# 설명: dp 

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        paths = [[0 for _ in range(n)] for _ in range(m)]

        paths[0][0] = grid[0][0]
        for i in range(1, n):
            paths[0][i] += paths[0][i-1] + grid[0][i]
        for i in range(1, m):
            paths[i][0] += paths[i-1][0] + grid[i][0]

        for r in range(1, m):
            for c in range(1, n):
                paths[r][c] = grid[r][c] + min(paths[r][c-1], paths[r-1][c])
        # for i in range(m):
        #     print(paths[i])

        return paths[m-1][n-1]