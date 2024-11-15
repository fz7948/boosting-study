# https://leetcode.com/problems/unique-paths/
# 백트래킹 문제로 0,0에서 해당지점까지 가는 문제로, 메트릭스로 플어도 되지만 간단하게 순열조합으로 풀었습니다. 

class Solution(object):
    def uniquePaths(self, m, n):
        import math
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return math.factorial(m+n-2)//(math.factorial(m-1) * math.factorial(n-1))
        