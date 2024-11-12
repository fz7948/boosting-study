# https://leetcode.com/problems/is-subsequence

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = j = 0
        if s == "":
            return True
        if len(s) > len(t):
            return False

        while j < len(t):
            if i < len(s) and s[i] == t[j]:
                i += 1
            j += 1
        
        if i < len(s):
            return False
        elif i == len(s):
            return True
        else:
            return False