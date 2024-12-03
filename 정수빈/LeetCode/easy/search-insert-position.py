# https://leetcode.com/problems/search-insert-position/?envType=study-plan-v2&envId=top-interview-150
# 설명: bst
# 시간: 2분 30초

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target <= nums[0]:
            return 0
        
        for i in range(1, len(nums)):
            if nums[i-1] <= target <= nums[i]:
                return i
        return len(nums)