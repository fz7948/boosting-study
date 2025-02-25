# https://leetcode.com/problems/confusing-number/
# 걸린 시간: 5분

class Solution:
    def confusingNumber(self, n: int) -> bool:
        n = str(n)
        s = ""
        for i in range(len(n)):
            if n[i] == "1":
                s = "1" + s
            elif n[i] == "0":
                s = "0" + s
            elif n[i] == "6":
                s = "9" + s
            elif n[i] == "8":
                s = "8" + s
            elif n[i] == "9":
                s = "6" + s
            else:
                return False
        return s != n