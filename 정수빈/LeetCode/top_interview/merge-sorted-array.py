# https://leetcode.com/problems/merge-sorted-array
# 설명: nums1의 0으로 채워진 배열에 nums2를 넣는 문제입니다. 
# 난이도: easy

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[i+m] = nums2[i]
        nums1.sort()

