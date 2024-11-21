# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
# 설명: 주식을 사고팔아서 이익이 최대로 하는 방법을 구하는 문제입니다. 
# 해결 x
# 난이도: medium

class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        
        return profit
