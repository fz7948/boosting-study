# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=study-plan-v2&envId=leetcode-75
# 시간: 5분
# 유형: Sliding Window, max-consecutive-ones-iii 문제 답을 참고해서 품
# 난이도: medium

class Solution:
    def longestSubarray(self, nums) -> int:
        lp = 0
        k = 1
        for rp in range(len(nums)):
            k -= 1 - nums[rp]

            if k < 0:
                k += 1 - nums[lp]
                lp += 1

        return rp - lp