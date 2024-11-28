# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        number = 0
        for i in range(n):
            number += digits[i]*10**(n-i-1)
        number += 1
        ans = []
        while number > 0:
            ans.append(number % 10)
            number = number // 10
        
        return ans[::-1]