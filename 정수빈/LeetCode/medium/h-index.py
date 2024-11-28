# https://leetcode.com/problems/h-index
# 난이도: medium
# 시간: 6분 45초

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        hinx = 0
        for i in range(len(citations), 0, -1):
            over_paper = list(filter(lambda x: x >= i, citations))
            if i <= len(over_paper):
                hinx = max(i, hinx)
        return hinx