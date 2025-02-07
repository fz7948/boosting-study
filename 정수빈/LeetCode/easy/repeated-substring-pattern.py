# https://leetcode.com/problems/repeated-substring-pattern
# 걸린시간: 5분

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ans = ""
        for i in range(len(s)-1):
            word = s[:i+1]
            check = True
            for t in set(s.split(word)):
                if len(t) > 0:
                    check = False
                    break
            if check:
                return True
        return False