# https://leetcode.com/problems/two-sum
# 설명: 두 수의 합이 target이 되는 수를 구하는 문제입니다.  
# 난이도: easy, 걸린시간 2분

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        