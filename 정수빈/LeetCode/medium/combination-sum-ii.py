# https://leetcode.com/problems/combination-sum-ii/
# 거의 다 풀었는데, 타임아웃 문제가 ㅠㅠ 답지를 보니까 candidates를 정렬하고, 중복되는 경우를 제외하면서 탐색해야 했나봄

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        candidates.sort()

        def bf(idx, total, elems = []):
            if idx == len(candidates):
                if total == target:
                    elems.sort()
                    ans.add(tuple(elems))
                return 
            
            if total == target:
                elems.sort()
                ans.add(tuple(elems))
                return 
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                if total + candidates[i] <= target:
                    bf(i+1, total+candidates[i], elems+[candidates[i]])
                else:
                    break

        bf(0, 0, [])
        ans = [list(e) for e in ans]
        return ans
