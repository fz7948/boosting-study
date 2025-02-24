# https://leetcode.com/problems/permutation-sequence

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        from itertools import permutations
        i = 1
        for row in permutations(list(range(1, n+1)), n):
            if i == k:
                return "".join(map(str,row))
            i += 1