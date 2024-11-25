# https://leetcode.com/problems/longest-palindromic-substring/
# 난이도 : medium
# 시간: x (해결못함)
# 설명: 긴 팔린드롬을 찾는 문제로 o(n2)까지 되지만.. 저는 o(n3)으로 처음 시도했을 때 타임아웃.., 
# 해답은 i를 기준으로 양 사이드로 퍼져가면서 팔린드롬을 찾으면 됩니다.

class Solution:

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        ans = ""
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > len(ans):
                    ans = s[l:r+1]
                l -= 1
                r += 1
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > len(ans):
                    ans = s[l:r+1]
                l -= 1
                r += 1
        return ans
                    
        