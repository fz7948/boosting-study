# https://leetcode.com/problems/valid-palindrome-iv/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency

class Solution:
    def makePalindrome(self, s: str) -> bool:
        lp = 0
        rp = len(s)-1
        k = 0

        while rp > lp:
            if s[lp] != s[rp]:
                k += 1
            rp -=1
            lp +=1
            
            if k > 2:
                return False
        return True