# https://leetcode.com/problems/maximum-ascending-subarray-sum/description/?envType=daily-question&envId=2025-02-04

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_ascending_elem = []

        cur_ascending_elem = set()
        cur_ascending_elem.add(nums[0])

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cur_ascending_elem.add(nums[i-1])
                cur_ascending_elem.add(nums[i])
            else:
                if sum(max_ascending_elem) < sum(cur_ascending_elem):
                        max_ascending_elem = cur_ascending_elem
                cur_ascending_elem = set()
                cur_ascending_elem.add(nums[i])

        return max(sum(cur_ascending_elem), sum(max_ascending_elem))
            