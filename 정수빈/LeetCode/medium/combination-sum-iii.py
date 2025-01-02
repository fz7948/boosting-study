# https://leetcode.com/problems/combination-sum-iii/description/?envType=study-plan-v2&envId=leetcode-75
# 유형: backtracking
# 시간: 15분

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = {}

        def bk(idx, total, elems=[]):
            if idx == k:
                if sum(elems) == n:
                    ans[tuple(sorted(elems))] = True
                return 
            
            s = elems[-1] if len(elems) else 1
            for i in range(max(s, 1), min(10,n)):
                if total + i <= n and not i in elems:
                    bk(idx+1, total + i, elems + [i])  


        bk(0, 0, [])    
        return list(ans.keys())  