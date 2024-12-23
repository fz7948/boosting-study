# https://leetcode.com/problems/minimum-falling-path-sum/?envType=study-plan-v2&envId=dynamic-programming

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        min_sum_grid = [[0 for _ in range(n)] for _ in range(n)]
        min_sum_grid[0] = matrix[0]

        for r in range(1, n):
            for c in range(n):
                tmp = []
                tmp.append(min_sum_grid[r-1][c])
                if 0 <= c-1 < n:
                    tmp.append(min_sum_grid[r-1][c-1])
                if 0 <= c+1 < n:
                    tmp.append(min_sum_grid[r-1][c+1])
                min_sum_grid[r][c] = min(tmp) + matrix[r][c]
        # print(min_sum_grid)
        return min(min_sum_grid[n-1])