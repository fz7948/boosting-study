# https://leetcode.com/problems/faulty-keyboard/?envType=company&envId=samsung&favoriteSlug=samsung-six-months
# 난이도: easy

class Solution:
    def finalString(self, s: str) -> str:
        p = 0
        while p < len(s):
            
            if s[p] == "i":
                s = s[:p][::-1] + s[p+1:]
            else:
                p += 1
        return s