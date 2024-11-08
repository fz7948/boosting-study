# https://leetcode.com/problems/longest-consecutive-sequence/
# 설명: 제일 긴 연속된 숫자의 길이를 구하는 문제
# 정렬 후, 이전 숫자와 현재 숫자 차이가 1이 나는 길이를 구한다. 그중에서 제일 긴 길이를 리턴한다

class Solution(object):
    def longestConsecutive(self, nums):
        nums = list(set(nums))
        nums.sort()
        maxLen = 1
        lenn = 1
        if not nums:
            return 0
        prevNum = nums[0]
        for n in nums[1:]:
            if n == prevNum +1:
                lenn +=1
                if lenn > maxLen:
                    maxLen = lenn
            else:
                lenn = 1
            prevNum = n
        return maxLen
