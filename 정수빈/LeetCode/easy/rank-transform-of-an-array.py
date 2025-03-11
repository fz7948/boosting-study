# https://leetcode.com/problems/rank-transform-of-an-array/

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(arr)
        order = {}
        i = 1
        for n in sorted_arr:
            if not n in order:
                order[n] = i
                i += 1
        ans = []
        for n in arr:
            ans.append(order[n])
        return ans