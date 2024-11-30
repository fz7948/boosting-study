# https://leetcode.com/problems/valid-anagram
# 설명: O(n2)에서 O(n)으로 번경 쳇지피티의 도움 껄껄
# 난이도: easy

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        return Counter(s) == Counter(t)
