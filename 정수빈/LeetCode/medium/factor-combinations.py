# https://leetcode.com/problems/factor-combinations
# 걸린시간 20분

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        ans = set()
        init_n = n
        def bk(n, factors, start):
            if n == 1 and len(factors) > 1:
                ans.add(tuple(sorted(factors)))
                return 

            for i in range(start, int(n ** 0.5) + 1):
                if n % i == 0:
                    bk(n // i, factors+[i], i)
                    
            if n >= start and n != init_n:
                ans.append(factors+[n])

        ans = []
        bk(n, [], 2)
        return ans