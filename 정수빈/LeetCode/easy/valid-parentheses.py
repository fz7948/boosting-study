# https://leetcode.com/problems/valid-parentheses
# 난이도: easy
# 시간: 2분

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in "{[(":
                stack.append(c)
            elif stack and c in "}" and stack[-1] == "{":
                stack.pop()
            elif stack and c in "]" and stack[-1] == "[":
                stack.pop()
            elif stack and c in ")" and stack[-1] == "(":
                stack.pop()
            else:
                return False

        if stack:
            return False
        else:
            return True                            
                