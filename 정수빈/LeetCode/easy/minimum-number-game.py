# https://leetcode.com/problems/minimum-number-game/

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        i = 0

        while nums:
            elem1 = min(nums)
            nums.remove(elem1)

            elem2 = min(nums)
            nums.remove(elem2)

            arr.append(elem2)
            arr.append(elem1)
        return arr