# https://leetcode.com/problems/find-the-highest-altitude/?envType=study-plan-v2&envId=leetcode-75
# 난이도: easy

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxHeight = gain[0]
        accum = 0
        for _, height in enumerate(gain):
            maxHeight = max(accum, maxHeight)
            accum += height
        maxHeight = max(accum, maxHeight)
        return maxHeight