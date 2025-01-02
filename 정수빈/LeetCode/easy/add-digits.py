# https://leetcode.com/problems/add-digits/?envType=problem-list-v2&envId=simulation
# 난이도: easy
# simulation

class Solution:
    def addDigits(self, num: int) -> int:
        str_num = str(num)
        ans = 0
        if len(str_num) == 1:
            return int(str_num)

        while len(str_num) > 1:
            ans = 0
            for i in range(len(str_num)):
                ans += int(str_num[i])
            str_num = str(ans)
        return ans