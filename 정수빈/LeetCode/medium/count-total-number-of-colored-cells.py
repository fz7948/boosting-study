# https://leetcode.com/problems/count-total-number-of-colored-cells/

class Solution:
    def coloredCells(self, n: int) -> int:
        curr = 1
        for i in range(n):
            curr += i * 4
        return curr