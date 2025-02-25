# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/
# 걸린시간 : 5분

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        
        while len(s) > 2: 
            c = ""
            for i in range(1, len(s)):
                c += str((int(s[i-1]) + int(s[i])) % 10)
            s = c
        return s[0] == s[1]