# url: https://leetcode.com/problems/rotate-image/
# 예전에 답을 봤는데도 못품 ㅠㅠㅠㅠ

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for i in range(n // 2 + n %2):
            for j in range(n // 2):
                tmp = matrix[n - 1 -j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp