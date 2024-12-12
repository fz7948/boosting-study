# https://leetcode.com/problems/climbing-stairs/?envType=study-plan-v2&envId=dynamic-programming
# 설명: dp
# 난이도: easy

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n + 1)
        def climb(i):
            if i > n:
                return 0
            if i == n:
                return 1
            if memo[i] > 0:
                return memo[i]
            memo[i] = climb(i + 1) + climb(i + 2)
            
            return memo[i]
        
        return climb(0)

