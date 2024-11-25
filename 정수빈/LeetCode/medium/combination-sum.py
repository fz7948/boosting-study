# https://leetcode.com/problems/combination-sum/
# 설명: 백트레킹을 이용하여 리스트 요소들의 합 == target 만드는 문제입니다. 
# 시간: 8분 21초
# 난이도: medium

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        ans = []
        def bk(total, candids):
            if total == target:
                candids
                ans.append(sorted(candids))
                return 
            elif total > target:
                return 
            
            for i in range(len(candidates)):
                can = candidates[i]
                bk(total + can, candids + [can])
        
        bk(0, [])

        ans = list(set(map(lambda x: tuple(x), ans)))
        return ans