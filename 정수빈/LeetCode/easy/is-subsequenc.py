# https://leetcode.com/problems/is-subsequenc

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        lp = 0
        for c in t:
            if c == s[lp]:
                lp += 1
                if lp >= len(s):
                    break
        
        return lp == len(s)