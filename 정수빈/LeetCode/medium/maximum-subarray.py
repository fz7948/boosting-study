# https://leetcode.com/problems/maximum-subarray/
# 걸린시간: 5분, 카데인 알고리즘 공부하고 다시 품!

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_value = [0] * len(nums)
        max_value[0] = nums[0]

        for i in range(1, len(nums)):
            max_value[i] = max(nums[i], nums[i] + max_value[i-1])

        return max(max_value)