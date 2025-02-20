# https://leetcode.com/problems/best-sightseeing-pair/

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_i = values[0]  # values[i] + i 의 최대값
        ans = float('-inf')
        n = len(values)

        for j in range(1, n):
            ans = max(ans, max_i + values[j] - j)  # 최댓값 업데이트
            max_i = max(max_i, values[j] + j)  # values[j] + j 최댓값 업데이트
        
        return ans