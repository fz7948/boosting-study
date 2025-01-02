# https://leetcode.com/problems/rotting-oranges/?envType=study-plan-v2&envId=leetcode-75
# 유형: dp
# 시간: 30분 

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        from collections import deque
        m = len(grid)
        n = len(grid[0])
        q = deque()
        visited = set()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                    visited.add((r, c))
        
        minute = 0

        while q:
            rr, cc, time = q.popleft()
            grid[rr][cc] = 2
            
            minute = max(minute, time)
            for dr, dc in direction:
                nr, nc = rr + dr, cc + dc
                if 0 <= nr < m and 0<= nc < n and grid[nr][nc] == 1 and not (nr, nc) in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc, time+1))

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    return -1
        return minute

