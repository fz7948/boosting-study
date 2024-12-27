from itertools import combinations

n, m = list(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
no_firewalls = []

for r in range(n):
    for c in range(m):
        if grid[r][c] == 0:
            no_firewalls.append((r,c))

from collections import deque

offset = [(1, 0), (0, 1), (-1, 0), (0, -1)]
q = deque()

def set_up_fire(visited, r, c):
    while q:
        r, c = q.popleft()
        for dr, dc in offset:
            nr = dr + r
            nc = dc + c
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0 and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = True

count = 0
max_area = 0
visited = [[False for _ in range(m)] for _ in range(n)]
for row in combinations(no_firewalls, 3):
    count += 1
    for r, c in row:
        grid[r][c] = 1

    for r in range(n):
        for c in range(m):
            visited[r][c] = False

    for r in range(n):
        for c in range(m):
            if grid[r][c] == 2 and not visited[r][c]:
                q.append((r, c))
                visited[r][c] = True
                set_up_fire(visited, r, c)

    count = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] == 0:
                count += 1

    max_area = max(max_area, count)

    for r, c in row:
        grid[r][c] = 0

print(max_area)