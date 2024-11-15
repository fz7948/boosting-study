# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
# 설명: 주식을 사서 최대 이익을 얻고 파는 문제입니다. 그냥 2중 loop을 쓰면 타임아웃이 납니다. 
# 최저가와 최고 이익을 기억하고 순회하면서 업데이트 해주면 되는 문제입니다. 
# 난이도가 easy인데도 모르면 풀기 어려운 문제인 거 같습니다. 
# 난이도: easy 

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        best_price = 0
        lowest_price = prices[0]
        for i in range(len(prices)):
            lowest_price = min(lowest_price, prices[i])
            best_price = max(best_price, prices[i]-lowest_price)
        return best_price