class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        lengrid = len(grid) - 2
        maxLocal = []
        for i in range(lengrid):
            row = []
            for j in range(lengrid):
                row.append(max(max(grid[i][j:j+3]), max(grid[i+1][j:j+3]), max(grid[i+2][j:j+3])))
            maxLocal.append(row)
        return maxLocal

Solution().largestLocal(grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]])

# [[9,9],[8,6]]