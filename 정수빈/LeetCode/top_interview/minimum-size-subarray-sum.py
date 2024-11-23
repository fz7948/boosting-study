# https://leetcode.com/problems/minimum-size-subarray-sum
# 문제를 잘 읽자.. 양의 정수로 구성된 배열이 주어져있다.
# target보다 같거나 큰 subarray를 구하는 것 subarray는 연속적인 수의 배열을 의미한다. 
# 포인터 내부의 합이 타겟보다 작다면 rp를 옮겨서 합산을 키워준다. 합산이 타겟보다 크다면 lp를 오른쪽으로 옮겨 
# subarray의 길이를 줄여준다. 

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        lp = 0
        rp = 0
        sum_ = nums[0]
        min_len = float("inf")
        while rp < len(nums):
            if sum_ < target:
                rp += 1
                if rp < len(nums):
                    sum_ += nums[rp]
            else:
                min_len = min(min_len, rp - lp+1)
                sum_ -= nums[lp]
                lp +=1
        if min_len == float("inf"):
            return 0
        return min_len
