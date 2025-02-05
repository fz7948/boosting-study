# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description/?envType=daily-question&envId=2025-02-03
# 걸린시간: 5분

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 0
        count = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
            else:
                ans = max(count, ans)
                count = 1
        ans = max(count, ans)
        count = 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                count += 1
            else:
                ans = max(count, ans)
                count = 1
        ans = max(count, ans)
        return ans
