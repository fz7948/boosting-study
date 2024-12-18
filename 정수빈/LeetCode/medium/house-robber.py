# https://leetcode.com/problems/house-robber/?envType=study-plan-v2&envId=dynamic-programming
# 난이도: medium
# 설명: dp, 잘 이해는 안가는데.. 암튼 이렇게 풀 수 있다고 합니다. 

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [0 for _ in range(len(nums))]

        for i in range(len(nums)):
            if i == 0:
                dp[0] = nums[0]
                continue
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return max(dp)