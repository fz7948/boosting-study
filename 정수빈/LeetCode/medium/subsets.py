# https://leetcode.com/problems/subsets/
# 걸린시간 7분

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def bk(idx, subset):
            if idx == len(nums):
                ans.append(subset)
                return 

            bk(idx+1, subset)
            bk(idx+1, subset+[nums[idx]])
        
        bk(0, [])
        return ans