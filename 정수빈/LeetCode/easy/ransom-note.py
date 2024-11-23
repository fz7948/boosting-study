# https://leetcode.com/problems/ransom-note/
# 난이도: easy

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        from collections import Counter
        cmg = Counter(magazine)
        rmg = Counter(ransomNote)

        for k, v in rmg.items():
            if not k in cmg:
                return False
            else:
                if cmg[k] < v:
                    return False
        return True
