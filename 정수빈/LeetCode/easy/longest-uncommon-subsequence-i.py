# https://leetcode.com/problems/longest-uncommon-subsequence-i/
# 가장 긴 uncommon subsequence의 길이를 구하는 문제이다.
# 두 문자열이 같으면 -1을 반환하고, 아니면 두 문자열 중 긴 문자열의 길이를 반환한다.

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        return max(len(a), len(b))

