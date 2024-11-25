# https://leetcode.com/problems/palindrome-number/
# 난이도: easy
# 시간: 2분
# 설명: 숫자 팔린드롬을 구하는 문제입니다. 

class Solution:
    def isPalindrome(self, x: int) -> bool:
        sx = str(x)
        lp = 0
        rp = len(sx) -1
        while lp < rp:
            if sx[lp] != sx[rp]:
                return False
            lp +=1
            rp -= 1
        return True