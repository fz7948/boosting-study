# https://leetcode.com/problems/maximum-sum-of-an-hourglass/description/?envType=daily-question&envId=2025-01-15
# leetcode 신상 문제 
# 난이도: medium

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_sum = 0
        m = len(grid)
        n = len(grid[0])

        for r in range(m-2):
            for c in range(n-2):
                s = sum([sum(grid[r][c:c+3]), sum(grid[r+1][c:c+3]), sum(grid[r+2][c:c+3])])
                s -= grid[r+1][c]
                s -= grid[r+1][c+2]
                max_sum = max(s, max_sum)
        return max_sum