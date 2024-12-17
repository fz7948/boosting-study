# https://leetcode.com/problems/min-cost-climbing-stairs/?envType=study-plan-v2&envId=dynamic-programming
# 설명: dp
# 난이도: easy

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [0] * (n + 1)
        for i in range(2, len(cost)+ 1):
            one_step = memo[i - 1] + cost[i - 1]
            two_step = memo[i - 2] + cost[i - 2]
            memo[i] = min(one_step, two_step)
        return memo[-1]