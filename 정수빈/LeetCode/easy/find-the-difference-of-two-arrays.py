# https://leetcode.com/problems/find-the-difference-of-two-arrays
# 설명: 두 배열의 차집합 각각 출력하는 문제입니다. 간단하게 파이썬 set을 이용하여 구현했습니다. 

class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        num1 = set(nums1)
        num2 = set(nums2)
        intersec_num1 = list(num1 - num2)
        intersec_num2 = list(num2 - num1)
        return [intersec_num1, intersec_num2]

        