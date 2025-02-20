# https://leetcode.com/problems/first-missing-positive
# 걸린시간 10분

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        from collections import Counter
        counter = Counter(nums)
        ans = float("inf")
        for n in range(1, len(counter)+1):
            if not n in counter:
                ans = min(ans, n)
        if ans == float("inf"):
            if len(nums) == 1:
                if nums[0] < 1:
                    return 1
                elif nums[0] == 1:
                    return 2
                else:
                    return 1
            else:
                return n+1
        return ans
