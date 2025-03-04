# https://leetcode.com/problems/apply-operations-to-an-array

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *=2
                nums[i+1] = 0
        from collections import Counter
        counter = Counter(nums)
        count = 0
        i = 0
        while i < len(nums) and count < counter[0]:
            if nums[i] == 0:
                n = nums.pop(i)
                nums.append(n)
                count += 1
            else:
                i += 1

        return nums