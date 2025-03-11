# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks
# 조금 더 효율적으로 푸는 방법이 있지만.. 일단은 이렇게 풀었다.
# 이 문제는 sliding window로 풀 수 있다.

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        from collections import Counter
        ans = len(blocks)
        for i in range(len(blocks) - k+1):
            ans = min(Counter(blocks[i:i+k])["W"], ans)
        return ans