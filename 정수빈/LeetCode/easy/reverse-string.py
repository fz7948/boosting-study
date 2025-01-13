# https://leetcode.com/problems/reverse-string/description/?envType=company&envId=apple&favoriteSlug=apple-three-months
# You must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        tmp = None
        n = len(s)
        for i in range(n//2):
            tmp = s[i]
            s[i] = s[n - i -1]
            s[n-i-1] = tmp
        