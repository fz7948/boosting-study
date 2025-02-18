# https://leetcode.com/problems/missing-ranges/
# 걸린시간 1시간 정도, 타임아웃, 메모리아웃이 나서 변수 하나로 사용하는 방법으로 바꿨습니다.

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        ans = []
        if not nums:
            return [[lower, upper]]

        if lower < nums[0]:
            ans.append([lower, nums[0] - 1])

        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            if diff > 1:
                ans.append([nums[i-1]+1, nums[i]-1])

        if upper > nums[-1]:
            ans.append([nums[-1]+1, upper])

        return ans
