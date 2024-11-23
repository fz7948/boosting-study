# https://leetcode.com/problems/roman-to-integer

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums_tb = {
            "I" : 1,
            "IV": 4,
            "IX": 9,
            "V": 5,
            "X": 10,
            "XL": 40,
            "XC": 90,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "CM": 900,
            "CD": 400,
        }
        ans = 0
        i = 0
        while i < len(s):
            if i+1 < len(s) and s[i:i+2] in ["IV", "IX", "XL", "XC", "CM", "CD"]:
                ans += nums_tb[s[i:i+2]]
                i += 2
            else:
                ans += nums_tb[s[i:i+1]]
                i += 1
        return ans
        