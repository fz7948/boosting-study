# https://leetcode.com/problems/combinations
# 설명: 백트레킹, 조합을 구하는 문제 
# 난이도: medium
# 시간: 답지보면서 32분..

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        n = list(range(1, n+1))
        ans = []
        
        def bk(idx, num):
            if len(num) == k:
                ans.append(num)
                return 
            
            for i in range(idx, len(n)):
                c = n[i]
                bk(i+1, num+[c])
        bk(0, [])
        return ans