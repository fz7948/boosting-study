# https://leetcode.com/problems/permutations-ii
# 걸린시간: 5분

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations

        return list(set(permutations(nums, len(nums))))