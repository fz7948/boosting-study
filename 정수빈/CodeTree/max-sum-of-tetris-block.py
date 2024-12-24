n, m = list(map(int, input().split()))

grid = [list(map(int, input().split())) for _ in range(n)]

max_total = 0

def move(count, r, c, visited=[], total=0):
    global max_total
    if count == 4:
        max_total = max(total, max_total)
        return 
    
    visited.append((r, c))
    total += grid[r][c]

    if not (r, c+1) in visited and 0 <= r < n and 0 <= c+1 < m:
        move(count+1, r, c+1, visited[:], total) 

    if not (r, c-1) in visited and 0 <= r < n and 0 <= c-1 < m:
        move(count+1, r, c-1, visited[:], total)

    if not (r+1, c) in visited and 0 <= r+1 < n and 0 <= c < m:
        move(count+1, r+1, c, visited[:], total)
        
    if not (r-1, c) in visited and 0 <= r-1 < n and 0 <= c < m:
        move(count+1, r-1, c, visited[:], total)
    
    if (r+1, c) in visited and (r+2, c) in visited and not (r+1, c+1) in visited and 0 <= r+1 < n and 0 <= c+1< m:
        move(count+1, r+1, c+1, visited[:], total)

    if (r+1, c) in visited and (r+2, c) in visited and not (r+1, c-1) in visited and 0 <= r+1 < n and 0 <= c-1< m:
        move(count+1, r+1, c-1, visited[:], total)

    if (r, c+1) in visited and (r, c+2) in visited and not (r+1, c+1) in visited and 0 <= r+1 < n and 0 <= c+1< m:
        move(count+1, r+1, c+1, visited[:], total)

    if (r, c+1) in visited and (r, c+2) in visited and not (r+1, c+1) in visited and 0 <= r-1 < n and 0 <= c+1< m:
        move(count+1, r-1, c+1, visited[:], total)

for r in range(n):
    for c in range(m):
        move(0, r, c, [], 0)
print(max_total)