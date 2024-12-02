# https://leetcode.com/problems/zigzag-conversion
# 난이도: medium

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        str_map = [["" for _ in range( len(s) )] for _ in range(numRows)]
        # for s in str_map:
        #     print(s)
        nx = 0
        ny = 0
        if numRows * 2 - 2 == 0:
            return s
        for i in range(len(s)):
            d = i % (numRows * 2 - 2)
            str_map[ny][nx] = s[i]
            if d < numRows -1:
                ny = ny + 1
            else:
                ny = ny - 1
                nx = nx + 1 
        ans = ""
        for s in str_map:
            ans += "".join(s)
        return ans