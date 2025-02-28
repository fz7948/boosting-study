# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray
# 난이도: medium
# 카데인 알고리즘

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxValues = [0] * len(nums) 
        minValues = [float("inf")] * len(nums) 
        maxValues[0] = nums[0]
        minValues[0] = nums[0]

        for i in range(1, len(nums)):
            maxValues[i] = max(nums[i], nums[i] + maxValues[i-1])
            minValues[i] = min(nums[i], nums[i] + minValues[i-1])

        a = max(maxValues)
        b = abs(min(minValues))
        return a if a > b else b