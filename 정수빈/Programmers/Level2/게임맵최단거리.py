def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    # 최단 거리 변수 초기화
    paths = []
    
    def dfs(x, y, path_len):
        
        # 목적지 도착 시 최단 경로 갱신
        if x == n - 1 and y == m - 1:
            paths.append(path_len)
            return
        
        # 방문 처리
        visited[x][y] = True
        
        # 4방향 탐색
        for dx, dy in offsets:
            nx, ny = x + dx, y + dy
            
            # 이동 가능한 위치 확인
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                dfs(nx, ny, path_len + 1)
        
        # 백트래킹: 다른 경로 탐색을 위해 방문 상태 되돌리기
        visited[x][y] = False
    
    # 시작점에서 탐색 시작
    if maps[0][0] == 1:
        dfs(0, 0, 1)
    
    if paths:
        return min(paths)
    else:
        return -1


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]), 11)
# print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]), -1)