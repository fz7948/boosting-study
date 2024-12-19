# https://leetcode.com/problems/unique-paths/?envType=study-plan-v2&envId=dynamic-programming
# 설명: dp, 예전에 순열로 풀었지만, 다시 dp로 풀었습니다. 

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[None for _ in range(n)] for _ in range(m)]
        for i in range(m):
            grid[i][0] = 1
        for i in range(n):
            grid[0][i] = 1

        for r in range(1, m):
            for c in range(1, n):
                grid[r][c] = grid[r][c-1] + grid[r-1][c]

        return grid[m-1][n-1]
        