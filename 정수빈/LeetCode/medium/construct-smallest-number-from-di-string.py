# https://leetcode.com/problems/construct-smallest-number-from-di-string
# 걸린시간 15분

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        digits = [1,2,3,4,5,6,7,8,9]
        self.ans = ""
        def bk(idx, num):
            if idx == len(pattern):
                if not self.ans:
                    self.ans = num
                else:
                    self.ans = min(self.ans, num)
                return 

            if pattern[idx] == "I":
                for i in range(len(digits)):
                    if int(num[-1]) < digits[i]:
                        n = digits[i]
                        digits.remove(n)
                        bk(idx + 1, num + str(n))
                        digits.insert(i, n)
            elif pattern[idx] == "D":
                for i in range(len(digits)):
                    if int(num[-1]) > digits[i]:
                        n = digits[i]
                        digits.remove(n)
                        bk(idx + 1, num + str(n))
                        digits.insert(i, n)
        
        for i in range(1, 10):
            digits.remove(i)
            bk(0, str(i))
            digits.insert(i-1, i)
        return self.ans