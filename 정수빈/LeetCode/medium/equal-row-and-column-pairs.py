# https://leetcode.com/problems/equal-row-and-column-pairs/?envType=study-plan-v2&envId=leetcode-75
# 시간: 7분 40초
# 난이도: medium
# hash table

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)

        dic = {}
        for i in range(n):
            row = tuple(grid[i])
            dic[row] = 1 + dic.get(row, 0)
        # print(dic)
        ans = 0
        for i in range(n):
            row = []
            for j in range(n):
                row.append(grid[j][i])
            if tuple(row) in dic:
                ans += dic[tuple(row)]
        return ans