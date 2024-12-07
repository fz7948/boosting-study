# https://leetcode.com/problems/string-to-integer-atoi/
# 빈도수 정렬
# 난이도: medium

class Solution:
    def myAtoi(self, s: str) -> int:
        num = ""
        sign = 1
        s = s.strip()
        for i, c in enumerate(s):
            if i == 0 and c == "+":
                sign = 1
            elif i == 0 and c == "-":
                sign = -1
            elif c in "1234567890":
                num += c
            else:
                break
        if num == "":
            num = 0
        
        num = int(num) * sign
        if num < -2**31:
            num = -2**31
        elif num >= 2**31-1:
            num = 2**31-1
        return num