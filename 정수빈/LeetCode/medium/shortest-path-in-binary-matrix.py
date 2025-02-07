# https://leetcode.com/problems/shortest-path-in-binary-matrix
# 걸린시간: 20분

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        from collections import deque
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        n = len(grid)
        q = deque()
        visited = set()
        if grid[0][0] == 0:
            q.append((0, 0, 1))
            visited.add((0, 0))

        while q:
            r,c, count = q.popleft()
            if r == n-1 and c == n-1:
                return count

            for dr, dc in directions:
                nr, nc, count = r + dr, c + dc, count
                if 0<= nr <n and 0<= nc <n and grid[nr][nc] == 0 and not (nr,nc) in visited:
                    visited.add((nr,nc))
                    q.append((nr, nc, count +1))
        return -1
            