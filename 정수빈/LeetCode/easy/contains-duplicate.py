# https://leetcode.com/problems/contains-duplicate/
# 걸린시간 : 5분

from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)

        for k, v in counter.items():
            if v > 1:
                return True
        return False