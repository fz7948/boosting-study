# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        from collections import deque

        paren_str = deque([])
        
        for i in range(len(s)):
            c = s[i]
            if c in "()":
                paren_str.append((c, i))
        # print(paren_str)
        if not paren_str:
            return s
        paren_q = [paren_str.popleft()]

        while paren_str:
            paren, idx = paren_str.popleft()
            if paren_q and paren_q[-1][0] == "(" and paren == ")":
                paren_q.pop()
            elif paren_q and paren_q[-1][0] == "(" and paren == "(":
                paren_q.append((paren, idx))
            else:
                paren_q.append((paren, idx))
        s = list(s)
        for _, idx in paren_q:
            s[idx] = " "
        s = [c for c in s if c != " "]
        return "".join(s)