# https://leetcode.com/problems/multiply-strings/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n = len(num1)
        m = len(num2)
        ten = 1
        total = 0
        for i in range(n-1, -1, -1):
            ten2 = 1
            for j in range(m-1, -1, -1):
                total += int(num1[i]) * int(num2[j]) * ten2 * ten
                ten2 *= 10
            ten *= 10
        return str(total)
