# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# 설명: 최소 2번은 나온 숫자를 지우는 문제입니다. 배열은 순서대로 정리되어 있습니다. 
# 난이도: medium

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = 0 
        curr = nums[0]
        while idx < len(nums)-2:
            if curr == nums[idx+1] and curr == nums[idx+2]:
                del nums[idx]
            else:
                idx += 1
            if idx < len(nums):
                curr = nums[idx]
        