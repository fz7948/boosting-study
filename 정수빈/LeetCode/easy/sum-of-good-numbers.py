# https://leetcode.com/problems/sum-of-good-numbers/
# 걸린시간 : 10분

class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            if 0 <= i-k and i+k < len(nums) and nums[i-k] < nums[i] and nums[i+k] < nums[i]:
                ans += nums[i]
            elif 0 <= i-k  and nums[i-k] < nums[i] and i+k+1 > len(nums):
                ans += nums[i]
            elif i+k < len(nums) and nums[i+k] < nums[i] and 0 > i-k:
                ans += nums[i]
            elif 0 > i-k and i+k+1 > len(nums):
                ans += nums[i]
        
        return ans