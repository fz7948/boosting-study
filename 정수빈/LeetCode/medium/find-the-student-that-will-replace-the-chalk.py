# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/
# 걸린시간 10분

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        i = 0
        k %= sum(chalk)
        while k > 0:
            k -= chalk[i]
            i += 1
            i %= len(chalk)
        if k == 0:
            return i
        else:
            return i-1 if i-1 >= 0 else len(chalk) - i -1
