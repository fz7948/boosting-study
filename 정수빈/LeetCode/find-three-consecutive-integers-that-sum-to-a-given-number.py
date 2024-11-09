# https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number
# 설명: num을 3개의 연속된 수로 표현하는 문제입니다. 

class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num % 3 == 0:
            m = num // 3
            return [m -1, m, m+1]
        else:
            return []