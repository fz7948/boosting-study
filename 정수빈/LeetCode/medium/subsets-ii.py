# https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        def bk(idx, subset):
            if idx == len(nums):
                ans.add(tuple(sorted(subset)))
                return 

            bk(idx+1, subset)
            bk(idx+1, subset+[nums[idx]])
        
        bk(0, [])
        ans = list(ans)
        ans.sort()
        return list(ans)