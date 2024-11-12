# https://leetcode.com/problems/reverse-vowels-of-a-string
# 설명: 자음만 순서를 바꿔 출력하는 문제입니다. 

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        idx_lst = []
        vowels_lst = []
        for i, c in enumerate(s):
            if c in ["a", "A", "e", "E", "i", "I", "u", "U", "o", "O"]:
                idx_lst.append(i)
                vowels_lst.append(c)
        vowels_lst = vowels_lst[::-1]
        s = list(s)
        for i, idx in enumerate(idx_lst):
            s[idx] = vowels_lst[i]
        
        return "".join(s)
        