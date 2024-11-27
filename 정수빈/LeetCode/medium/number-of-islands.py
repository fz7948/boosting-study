# https://leetcode.com/problems/number-of-islands/
# 설명: dfs, bfs문제 
# 해결못함
# 프로그래머스에서 푼 문제인데 동일한 문제인데도 못풀었네요 ㅠㅠ 정말 bfs, dfs는 어려운거 같습니다. ㅠㅠㅠ

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        from collections import deque


        visited = [[False for _ in range(n)] for _ in range(m)]
        offset = [(1, 0), (0, 1), (-1,0), (0, -1)]


        def dfs(y_, x_):
            print("y_, x_",y_, x_)
            queue = deque([(y_,x_)])
            visited[y_][x_] = True

            while queue:
              y, x = queue.popleft()

              for dy, dx in offset:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[ny][nx] and grid[ny][nx] == "1":
                        queue.append((ny, nx))
                        visited[ny][nx] = True

        ans = 0
        for y in range(m):
            for x in range(n):
                if grid[y][x] == "1" and not visited[y][x]:
                    print(y, x)
                    dfs(y, x)
                    ans +=1
        return ans
                    

