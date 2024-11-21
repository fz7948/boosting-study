# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
# 난이도: medium
# 시간: 5분

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        lp = 0
        rp = len(numbers) -1
        while lp < rp:
            summ = numbers[lp] + numbers[rp]
            if summ < target:
                lp += 1
            elif summ > target:
                rp -= 1
            else:
                return [lp+1, rp+1]