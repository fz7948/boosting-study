# https://leetcode.com/problems/the-kth-factor-of-n/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency
# 난이도: medium 하지만 매우 쉬웠습니다
# 시간: 5분

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, n+1):
            if n % i == 0:
                factors.append(i)
        
        if k-1 > len(factors) -1:
            return -1
        else:
            return factors[k-1]