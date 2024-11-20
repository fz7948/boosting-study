# https://leetcode.com/problems/remove-element
# 설명: nums에서 val을 제거하는 문제, 파이썬의 remove 함수를 사용해서 구현했습니다.
# 난이도: easy

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for _ in range(len(nums)):
            try:
                nums.remove(val)
            except:
                break
        