# https://leetcode.com/problems/coin-change/
# 걸린시간: 40분, 답지봄, 효율성 통과 안됨 ㅠ, dp는 항상 어려운거같다. 
# 근데 나 리트코드에서 bfs로 태그해서 푼건데 왜 dp가..
# amount가 10000 이하라서 가능한 문제일지도.. dp의 크기거 너무 큼 ㅠㅠ

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1 