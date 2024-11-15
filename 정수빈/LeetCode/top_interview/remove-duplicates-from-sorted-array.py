# https://leetcode.com/problems/remove-duplicates-from-sorted-array
# 설명: 중복된 요소를 in place로 제거하는 문제입니다. list, set을 사용하지 않고 구현했습니다. 배열은 순서대로 정리되어 있습니다. 
# 난이도: easy 

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = 0 
        curr = nums[0]
        while idx < len(nums)-1:
            if curr == nums[idx+1]:
                del nums[idx]
            else:
                idx += 1
            if idx < len(nums):
                curr = nums[idx]
        