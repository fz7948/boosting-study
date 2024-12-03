# https://leetcode.com/problems/search-a-2d-matrix/?envType=study-plan-v2&envId=top-interview-150
# 설명: bst
# 시간: 7분 30초

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        target_row = -1
        m = len(matrix)
        n = len(matrix[0])
        if target == matrix[0][0]:
            target_row = 0
        for i in range(1, m):
            if matrix[i-1][0] <= target < matrix[i][0]:
                target_row = i-1
        
        if target_row == -1:
            target_row = m-1

        row = matrix[target_row]
        for i in range(n):
            if row[i] == target:
                return True
        
        return False
        
