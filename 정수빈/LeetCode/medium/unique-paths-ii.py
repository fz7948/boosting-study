# https://leetcode.com/problems/unique-paths-ii/?envType=study-plan-v2&envId=dynamic-programming
# 설명: dp

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        unique_paths = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            unique_paths[i][0] = 1
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            unique_paths[0][i] = 1
        
        for r in range(1, m):
            for c in range(1, n):
                if obstacleGrid[r][c] == 1:
                    continue
                unique_paths[r][c] = unique_paths[r][c-1] + unique_paths[r-1][c]

        return unique_paths[m-1][n-1]