# https://leetcode.com/problems/product-of-array-except-self
# 난이도: medium

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroIndice = set()
        dot = 1
        for i, n in enumerate(nums):
            if n != 0:
                dot *= n
            else:
                zeroIndice.add(i)

        if len(zeroIndice) > 1:
            return [0 for _ in range(len(nums))]
        
        elif len(zeroIndice) == 0:
            return [dot // nums[i] for i in range(len(nums))]
        
        ans = []
        zeroIdx = list(zeroIndice)[0]
        for i in range(len(nums)):
            if i == zeroIdx:
                ans.append(dot)
            else:
                ans.append(0)
        return ans
                