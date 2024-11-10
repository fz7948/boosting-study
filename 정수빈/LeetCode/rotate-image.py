# https://leetcode.com/problems/rotate-image/
# 설명: n x n 크기의 2D 행렬을 90도 회전시키는 문제입니다. 
# left, right, top, bottom의 위치를 표시하고, 가장 모서리부터 회전시킵니다. 이거 설명하기 어렵네여 ㅠㅠㅠ 
# 도움이 많이 되었던 https://www.youtube.com/watch?v=BJnMZNwUk1M 유튜브 링크 첨부합니다. 

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        left = 0
        right = len(matrix)-1

        while True:
            for i in range(right - left): 
                top, bottom = left, right
                topLeft = matrix[top][left+i]
                matrix[top][left+i] = matrix[bottom-i][left]

                matrix[bottom-i][left] = matrix[bottom][right-i]

                matrix[bottom][right-i] = matrix[top+i][right] 

                matrix[top+i][right] = topLeft
            right -= 1
            left += 1
            if left >= right:
                break 
