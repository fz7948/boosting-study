# https://leetcode.com/problems/break-a-palindrome/

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)

        if 1 == len(palindrome):
            return ""

        for i in range(len(palindrome)):
            if palindrome[i] > "a" and not i == len(palindrome)//2:
                palindrome = list(palindrome)
                palindrome[i] = "a"
                return "".join(palindrome)

        palindrome = list(palindrome)
        palindrome[n-1] = "b"
        return "".join(palindrome)