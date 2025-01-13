# https://leetcode.com/problems/substring-matching-pattern/
# easy중에 정답률이 낮은 문제 

class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        p = p.split("*")
        n = len(s)
        for i in range(n):
            if p[0] == s[i:i+len(p[0])]:
                if p[1] == "":
                    return True
                for j in range(i+len(p[0]), n):
                    if p[1] == s[j:j+len(p[1])]:
                        return True
        return False
