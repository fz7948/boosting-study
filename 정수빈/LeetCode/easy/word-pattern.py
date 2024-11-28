# https://leetcode.com/problems/word-pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_map = {}
        n = len(pattern)
        ss = s.split(" ")
        if n != len(ss):
            return False
        for i in range(n):
            if not pattern[i] in word_map and not ss[i] in word_map.values():
                word_map[pattern[i]] = ss[i]
            elif not pattern[i] in word_map:
                return False
            else:
                if word_map[pattern[i]] != ss[i]:
                    return False
        return True