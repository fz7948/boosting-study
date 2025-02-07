# https://leetcode.com/problems/find-the-difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        for i in range(len(t)):
            if i < len(s) and not t[i] == s[i]:
                return t[i]
        return t[-1]