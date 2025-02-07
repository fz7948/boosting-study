# https://leetcode.com/problems/sign-of-the-product-of-an-array
# 걸린시간: 3분

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        neg = len(list(filter(lambda x: x<0, nums)))
        if neg % 2 == 0:
            return 1
        else:
            return -1