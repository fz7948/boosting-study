# https://leetcode.com/problems/permutations/
# 설명: permute을 백트레킹으로 구현하는 문제입니다. 
# 난이도: medium
# 시간: 15분 30초

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        def bk(case = [], nnums = []):
            if not nnums:
                ans.append(case)
                return 

            for i in range(len(nnums)):
                new_nums = nnums[:]
                n = nnums[i]
                new_nums.remove(n)
                bk(i+1, case + [nnums[i]], new_nums)
            
        bk(0, [], nums)
        return ans