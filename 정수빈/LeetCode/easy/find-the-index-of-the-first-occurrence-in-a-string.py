# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string
# 난이도: easy

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)