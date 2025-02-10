# https://leetcode.com/problems/shortest-bridge/description/?envType=problem-list-v2&envId=depth-first-search
# 걸린시간 : 1시간
# 자꾸 타임아웃이 났는데, 중간에 return을 안해줘서 그랬다.

from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        n = len(grid)
        def bfs(r, c):
            q = deque()
            q.append((r,c))
            visited = set()
            visited.add((r,c))

            while q:
                r, c = q.pop()
                visited.add((r, c))

                for dr, dc in directions:
                    nr, nc = dr+r, dc+c
                    if 0 <= nr < n and 0<= nc < n:
                        if grid[nr][nc] == 1 and not (nr, nc) in visited:
                            q.append((nr, nc))
                            visited.add((nr, nc))
            return visited

        def find_bridge(r, c, second_island):
            q = deque()
            q.append((r,c,0))
            visited = set()
            visited.add((r,c))
            ans = float("inf")
            while q:
                r, c, count = q.popleft()
                visited.add((r, c))

                for dr, dc in directions:
                    nr, nc, ncount = dr+r, dc+c, count+1
                    if (nr, nc) in second_island:
                        return count

                    if 0 <= nr < n and 0<= nc < n:
                        if grid[nr][nc] == 0 and not (nr, nc) in visited:
                            q.append((nr, nc, ncount))
                            visited.add((nr, nc))
            return ans

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    first_island = bfs(i, j)
                    break

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and not (i, j) in first_island:
                    second_island = bfs(i, j)
                    break

        ans = float("inf")
        for (r, c) in first_island:
            ans = min(ans, find_bridge(r, c, second_island))
        return ans
                