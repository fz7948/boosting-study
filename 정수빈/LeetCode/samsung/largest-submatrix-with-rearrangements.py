# https://leetcode.com/problems/largest-submatrix-with-rearrangements/?envType=company&envId=samsung&favoriteSlug=samsung-all
# 난이도: medium
# 해결 x 

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        res = 0
        prev_heights = [0] * COLS
        for r in range(ROWS):
            heights = matrix[r][::]
            for c in range(COLS):
                if heights[c] > 0:
                    heights[c] += prev_heights[c]
            
            sorted_heights = sorted(heights, reverse=True)
            for i in range(COLS):
                res = max(res, (i+1) * sorted_heights[i])
            prev_heights = heights
        return res

        