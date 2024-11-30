# https://leetcode.com/problems/isomorphic-strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        char_map = {}
        for i in range(n):
            if not s[i] in char_map and not t[i] in char_map.values():
                char_map[s[i]] = t[i]
            else:
                if not s[i] in char_map:
                    return False
                if char_map[s[i]] != t[i]:
                    return False
        return True