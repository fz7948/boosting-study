# https://leetcode.com/problems/fibonacci-number/?envType=study-plan-v2&envId=dynamic-programming
# 설명: dp
# 난이도: easy

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        memo = [0] * (n + 1)
        memo[0] = 0
        memo[1] = 1
        for i in range(1, n):
            memo[i+1] = memo[i] + memo[i-1]
        return memo[n]