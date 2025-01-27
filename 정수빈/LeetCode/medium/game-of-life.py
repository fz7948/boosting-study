# https://leetcode.com/problems/game-of-life/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        offset = [(-1, 0), (-1, 1), (-1, -1), (1, -1), (1 , 0), (1, 1), (0, -1), (0, 1)]
        m = len(board)
        n = len(board[0])

        next_dies = set()
        next_lives = set()
        for r in range(m):
            for c in range(n):
                count = 0
                for dr, dc in offset:
                    nr, nc = r+dr, dc+c
                    if not (0<= nr < m and 0 <= nc < n):
                        continue
                    if board[nr][nc] == 1:
                        count += 1
                if board[r][c] == 1 and count < 2:
                    next_dies.add((r, c))
                elif board[r][c] == 1 and count > 3:
                    next_dies.add((r, c))
                elif board[r][c] == 1 and 2 <= count < 4:
                    next_lives.add((r, c))
                elif board[r][c] == 0 and count == 3:
                    next_lives.add((r, c))
        
        for r, c in next_dies:
            board[r][c] = 0
        for r, c in next_lives:
            board[r][c] = 1
