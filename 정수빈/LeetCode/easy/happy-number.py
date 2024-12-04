# https://leetcode.com/problems/happy-number/?envType=study-plan-v2&envId=top-interview-150
# 시간: 4분 40초
# 난이도: easy

class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        ret = str(n)
        while ret != "1":
            nextn = 0
            for c in ret:
                nextn += int(c) * int(c)
            if not nextn in visited:
                visited.add(nextn)  
            else:
                return False
            ret = str(nextn)
        return True
