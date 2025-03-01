# https://leetcode.com/problems/koko-eating-bananas/
# 간만에 binary search 인데, 잘 못 풀었다. 오랜만에 해서 잘 못 푼 것 같다.
# 답지 봄

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            count = 0
            middle = (left + right) // 2

            for pile in piles:
                count += pile // middle 
                if pile % middle > 0:
                    count += 1
            
            if count <= h:
                right = middle
            else:
                left = middle + 1
            
        return right