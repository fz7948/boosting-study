# https://leetcode.com/problems/jump-game-ii
# 최선의 방법은 아니다, 최선은 그리디 알고리즘을 사용해야 한다. dfs로 풀었을 때 시간복잡도가 O(2^n)이기 때문에 시간초과가 난다. 그래서 추가로 메모이제이션을 사용해야 한다.
# 메모이제이션은 지피티한테 물어봄

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n  

        def bf(idx):
            if idx >= n - 1:
                return 0
            if dp[idx] != -1:
                return dp[idx]
            
            min_count = float("inf")
            for i in range(1, nums[idx] + 1):
                min_count = min(min_count, 1 + bf(idx + i))
            
            dp[idx] = min_count  # 메모이제이션
            return dp[idx]

        return bf(0)
