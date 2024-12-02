# https://leetcode.com/problems/spiral-matrix/
# top interview
# 난이도: medium

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        n = len(matrix)
        m = len(matrix[0])
        vistied = []
        route = []
        xy = (0, 0)
        di = 0
        while len(route) < n * m:
            if not xy in vistied:
                vistied.append(xy)
                route.append(matrix[xy[0]][xy[1]])
            dy, dx = d[di]
            ny, nx = xy[0] + dy, xy[1] + dx
            if 0 <= ny < n and 0 <= nx < m and not (ny, nx) in vistied:
                xy = (ny, nx)
            else:
                di += 1
                if di > 3:
                    di = 0
        
        return route

