# https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        
        def recurive(num):
            if num == 1:
                return "1"
            
            prev = recurive(int(num)-1)
            ans = ""
            order = ""
            prev_c = prev[0]
            count = 1
            for i in range(1, len(prev)):
                if prev_c == prev[i]:
                    count += 1
                else:
                    ans += str(count) + prev_c
                    prev_c = prev[i]
                    count = 1
            ans += str(count) + prev_c
            return ans
        return recurive(n)
            