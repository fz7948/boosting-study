# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxCandy = max(candies)
        ans = []
        for candy in candies:
            if candy + extraCandies >= maxCandy:
                ans.append(True)
            else:
                ans.append(False)
        return ans
        