# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/

class Solution:
    def minLength(self, s: str) -> int:
        
        while "AB" in s or "CD" in s:
            s = "".join(s.split("AB"))
            s = "".join(s.split("CD"))
        return len(s)