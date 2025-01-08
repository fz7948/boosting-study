# https://leetcode.com/problems/single-number/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter

        counter = Counter(nums)
        for k, v in counter.items():
            if v == 1:
                return k