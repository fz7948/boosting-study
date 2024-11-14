# https://leetcode.com/problems/removing-stars-from-a-string/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        idx = 0
        while idx < len(s):
            if not s[idx] == "*":
                stack.append(s[idx])
            else:
                stack.pop()
            idx +=1
        return "".join(stack)

        