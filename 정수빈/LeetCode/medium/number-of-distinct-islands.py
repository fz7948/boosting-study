# https://leetcode.com/problems/number-of-distinct-islands/description/?envType=problem-list-v2&envId=breadth-first-search
# bfs로 풀면 시간초과, dfs로 풀면 safe
# 시간: 30분

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        from collections import deque
        off_r = [-1, 1, 0, 0]
        off_c = [0, 0, -1, 1]
        m = len(grid)
        n = len(grid[0])
        visited = set()
        islands = set()
        q = deque()

        def search(r, c):
            q.append((r, c))
            island = set()
            min_r, min_c = r, c

            while q:
                r, c = q.pop()
                visited.add((r, c))
                island.add((r,c))
                min_r = min(min_r, r)
                min_c = min(min_c, c)
                for dr, dc in zip(off_r, off_c):
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < m and 0 <= nc < n and not (nr, nc) in visited and grid[nr][nc] == 1:
                        q.append((nr, nc))
            
            island_reguler = sorted((map(lambda x: (x[0]-min_r, x[1]-min_c), island)))
            islands.add(tuple(island_reguler))
        
        for r in range(m):
            for c in range(n):
                if not (r, c) in visited and grid[r][c] == 1:
                    search(r, c)
        # print(islands)
        return len(islands)