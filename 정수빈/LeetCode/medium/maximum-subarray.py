# https://leetcode.com/problems/maximum-subarray/
# 걸린시간: 10분, 근데 타임아웃나서 답지보고 다시품
# Dynamic Programming, Kadane's Algorithm 이라고 유명한 알고리즘을 사용하는 문제

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_subarray = max_subarray = nums[0]

        # Start with the 2nd element since we already used the first one.
        for num in nums[1:]:
            # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)

        return max_subarray