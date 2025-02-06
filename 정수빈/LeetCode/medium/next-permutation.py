# https://leetcode.com/problems/next-permutation/description/
# 걸린시간: 40분, 아이디어는 있었지만, 결국 답지봄

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return nums
        i = n - 2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1
        print(i)

        if i >= 0:
            j = n -1
            while nums[j] <= nums[i]:
                j -= 1
            temp = nums[i]
            nums[i] = nums[j] 
            nums[j] = temp
        i += 1
        j = n - 1
        while i < j:
            temp = nums[i]
            nums[i] = nums[j] 
            nums[j] = temp
            i += 1
            j -= 1
        return nums
                
    