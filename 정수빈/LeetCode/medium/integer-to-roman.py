# https://leetcode.com/problems/integer-to-roman/
# 난이도: medium

class Solution:
    def intToRoman(self, num: int) -> str:
        value_map = {
            "1": "I",
            "5": "V",
            "10": "X",
            "50": "L",
            "100": "C",
            "500": "D",
            "1000": "M"
        }

        digit = 1
        ans = []
        while num > 0:
            num_str = ""
            # print("num",num, num % 10)
            if num % 10 <= 3:
                num_str = value_map[str(10**(digit-1))] * (num % 10)
            elif num % 10 == 4:
                num_str =  value_map[str(10**(digit-1))] + value_map[str(10**digit//2)]
            elif num % 10 == 5:
                num_str = value_map[str(10**digit//2)]
            elif num % 10 <= 8:
                num_str = value_map[str(10**digit//2)] + value_map[str(10**(digit-1))] * ((num-5) % 10)
            else:
                num_str = value_map[str(10**(digit-1))] + value_map[str(10**(digit))]
            num //= 10
            digit +=1
            # print(num_str)
            ans.append(num_str)
        # print(ans)

        return "".join(ans[::-1])
