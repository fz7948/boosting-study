# https://leetcode.com/problems/n-th-tribonacci-number/
# 시간: 4분 40초
# 난이도: easy
# 설명: 3th 피보나치를 구하는 수입니다. 쉬운 dp입니다. 

class Solution:
    def tribonacci(self, n: int) -> int:
        t = []
        t.extend([0, 1, 1])
        
        if n == 0 :
            return 0
        elif n == 2 or n == 1:
            return 1
        
        for i in range(2, n):
            tn = t[i-2] + t[i-1] + t[i]
            t.append(tn)
        
        return t[-1]

        