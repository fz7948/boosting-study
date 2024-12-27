n, m = list(map(int, input().split()))

r, c, d = list(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
# 0 1 2 3 
# 북,동,남,서
offset = [(-1, 0), (0, 1), (1, 0), (0, -1)]
left = [3, 0, 1, 2]

def move(r, c, d):
    nd = left[d]
    dr, dc = offset[nd]
    nr, nc, nd = r+dr, c+dc, nd
    if 0<= nr < n and 0 <= nc < m:
        if not visited[nr][nc] and grid[nr][nc] == 0:
            visited[nr][nc] = True
            return nr, nc, nd
        else:
            for _ in range(3):
                nd = left[nd]
                dr, dc = offset[nd]
                nr, nc, nd = r+dr, c+dc, nd
                if 0<= nr < n and 0 <= nc < m:
                    if not visited[nr][nc] and grid[nr][nc] == 0:
                        visited[nr][nc] = True
                        return nr, nc, nd
    
    dr, dc = offset[d]
    return r-dr, c-dc, d
    
visited[r][c] = True
while True:
    r, c, d = move(r, c, d)
    if grid[r][c] == 1:
        break

count = 0
for r in range(n):
    for c in range(m):
        if visited[r][c]:
            count += 1

print(count)
