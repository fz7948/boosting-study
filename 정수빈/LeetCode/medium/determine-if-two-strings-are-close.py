# https://leetcode.com/problems/determine-if-two-strings-are-close/?envType=study-plan-v2&envId=leetcode-75
# 시간: 4분 20초

from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter_word1 = Counter(word1)
        counter_word2 = Counter(word2)
        
        word1_key = sorted(Counter(word1).keys())
        word2_key = sorted(Counter(word2).keys())
        if word1_key != word2_key:
            return False
        
        word1_value = sorted(Counter(word1).values())
        word2_value = sorted(Counter(word2).values())

        if word1_value != word2_value:
            return False
        return True