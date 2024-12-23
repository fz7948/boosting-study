# https://leetcode.com/problems/maximal-square/?envType=study-plan-v2&envId=dynamic-programming
# 시간: 25분
# 난이도: medium

class Solution:
    import math
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        sum_matrix = [[0 for _ in range(n)] for _ in range(m)]
        max_sum = 0
        sum_matrix[0] = list(map(int, matrix[0]))
        max_sum = max(sum_matrix[0])
        for c in range(m):
            sum_matrix[c][0] = int(matrix[c][0])
            if sum_matrix[c][0] == 1:
                max_sum = 1

        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == "1":
                    if matrix[r-1][c-1] =="1" and matrix[r][c-1] =="1" and matrix[r-1][c] =="1":
                        sum_matrix[r][c] = (math.sqrt(min([sum_matrix[r-1][c-1], sum_matrix[r-1][c], sum_matrix[r][c-1]])) + 1) ** 2
                    else:
                        sum_matrix[r][c] = int(matrix[r][c])
                    max_sum = max(max_sum, sum_matrix[r][c])

        return int(max_sum)
                    
                