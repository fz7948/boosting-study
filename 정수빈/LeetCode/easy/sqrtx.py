# https://leetcode.com/problems/sqrtx
# 설명: 야매 바이너리 서치로 품, 수학적으로는 0(1)로 푸는 방법도 있음

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        
        n = x // 2
        while n * n > x:
            n //= 2
        
        n *= 2
        while n * n > x:
            n -= 1
        
        return n 