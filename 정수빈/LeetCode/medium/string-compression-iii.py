# https://leetcode.com/problems/string-compression-iii/

class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        count = 0
        q = []
        for c in word:
            if not q:
                q.append(c)
                count = 1
                continue
            if c == q[-1] and count < 9:
                count += 1
            elif  c == q[-1] and count > 9:
                comp += str(count) + q.pop()
                count = 1
                q.append(c)
            else:
                comp += str(count) + q.pop()
                q.append(c)
                count = 1
        if q:
            comp += str(count) + q.pop()
        return comp            
            