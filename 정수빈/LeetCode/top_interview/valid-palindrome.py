# https://leetcode.com/problems/valid-palindrome/
# 시간: 4분 30초

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        new_s = ""
        for c in s:
            if str.isalpha(str(c)) or str.isdigit(str(c)):
                new_s += c
        lp = 0
        rp = len(new_s) - 1
        while lp <= rp:
            if new_s[lp] != new_s[rp]:
                return False
            lp += 1
            rp -= 1
        return True
        