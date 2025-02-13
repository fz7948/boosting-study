class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from collections import Counter

        counter = sorted(Counter(nums).items())
        
        idx = 0
        for n, count in counter:
            for i in range(idx, idx+count):
                nums[i] = n
            idx += count