# https://leetcode.com/problems/surrounded-regions/?envType=study-plan-v2&envId=top-interview-150
# 난이도: medium
# 시간: 49분

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        d = [(0, 1), (1,0), (0, -1),(-1, 0)]
        m = len(board[0])
        n = len(board)
        all_visited = set()
        def dfs(y, x, vistied=set()):
            stack = []
            stack.append((y,x))

            while stack:
                sy, sx = stack.pop()
                vistied.add((sy, sx))
                all_visited.add((sy, sx))
                for dy, dx in d:
                    nx = sx + dx
                    ny = sy + dy

                    if 0 <= nx < m and 0<= ny < n and \
                    board[ny][nx] == "O" and not (ny, nx) in vistied:
                        stack.append((ny,nx))
            return list(vistied)
        
        area = []
        for x in range(m):
            for y in range(n):
                if board[y][x] == "O" and not (y, x) in all_visited:
                    area.append(dfs(y, x, set()))
        
        for a in area:
            check = True
            for y, x in a:
                for dy, dx in d:
                    ny, nx = dy + y, dx + x
                    if not (0<=ny<n and 0<=nx<m):
                        check=False
                        break
            for y, x in a:
                if check:
                    board[y][x] = "X"

        return board