# https://leetcode.com/problems/excel-sheet-column-title/

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        base = 26
        ans = ""
        alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        while columnNumber > 0:
            columnNumber -= 1
            ans = alpha[columnNumber % base] + ans
            columnNumber //= base
        return ans