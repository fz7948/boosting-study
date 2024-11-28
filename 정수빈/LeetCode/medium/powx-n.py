# https://leetcode.com/problems/powx-n

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n > 0:
            ans = x
            count = 1
            while count < n:
                ans *= ans
                count += count
            for i in range(count-n):
                ans /= x
            return ans
        elif n < 0:
            ans = 1 / x
            count = 1
            while count < -n:
                ans *= ans
                count += count
            for i in range(count+n):
                ans *= x
            return ans