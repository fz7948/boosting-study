# https://leetcode.com/problems/divide-two-integers/
# 걸린시간: 10분

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor * dividend > 0:
            ans = dividend // divisor 
            return ans if ans < 2**31-1 else 2**31-1
        elif dividend % divisor == 0:
            return dividend // divisor
        else:
            ans = dividend // divisor +1
            return ans if ans > -2**31-1 else -2**31-1
