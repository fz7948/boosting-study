# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/description/?envType=study-plan-v2&envId=leetcode-75

from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = deque([])
        q.append(entrance+[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m = len(maze)
        n = len(maze[0])
        visited = set()

        while q:
            r, c, count = q.popleft()
            visited.add((r,c))
            for dr, dc in directions:
                nr, nc = r+dr, c+dc

                if 0<= nr < m and 0<= nc < n and maze[nr][nc] == "." and not (nr, nc) in visited:
                    if (nr == 0 or nr == m-1 or nc == 0 or nc == n-1) and [nr, nc] != entrance:
                        return count + 1
                    q.append((nr, nc, count+1))
                    visited.add((nr,nc))
        return -1 