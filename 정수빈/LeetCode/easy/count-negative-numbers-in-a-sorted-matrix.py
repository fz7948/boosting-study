# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/?envType=study-plan-v2&envId=binary-search
# 바이너리 서치문제인데 그냥 brute force로 품


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            for r in row:
                if r < 0:
                    count += 1
        return count
    
# class Solution:
#     def countNegatives(self, grid: List[List[int]]) -> int:
#         count = 0
#         n = len(grid[0])
#         for row in grid:
#             left, right = 0, n - 1
#             while left <= right:
#                 mid = (right + left) // 2
#                 if row[mid] < 0:
#                     right = mid - 1
#                 else:
#                     left = mid + 1
#             count += (n - left)
#         return count