# https://leetcode.com/problems/minimize-xor/
# leetcode 신상 문제 
# 난이도: medium

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bits_num = str(bin(num2)).count("1")
        b_num1 = bin(num1)[2:]

        ans = ["0" for _ in range(max(len(bin(num1)), len(bin(num2)))) ]
        for i in range(len(b_num1)):
            if b_num1[i] == "1" and bits_num > 0:
                ans.append("1")
                bits_num -= 1
            else:
                ans.append("0")

        if bits_num > 0:
            for i in range(len(ans)-1, -1, -1):
                if ans[i] == "0" and bits_num:
                    ans[i] = "1"
                    bits_num -= 1
                elif bits_num == 0:
                    break
        return int("".join(ans),2)