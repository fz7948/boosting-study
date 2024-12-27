# https://leetcode.com/problems/word-search/?envType=problem-list-v2&envId=backtracking
# 설명: bk

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        global ans
        ans = False

        
        def bk(idx, r, c):
            global ans
            if idx == len(word)-1:
                ans = True
                return 
            
            for dr, dc in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                nr, nc = r+dr, c+dc
                if 0<= nr < n and 0<= nc < m and not (nr, nc) in visited and word[idx+1] == board[nr][nc]:
                    visited.append((nr, nc))
                    bk(idx+1, nr, nc)
                    visited.pop()
        
        for r in range(n):
            for c in range(m):
                if board[r][c] == word[0]:
                    visited = [(r, c)]
                    bk(0, r, c)
                if ans:
                    break
        return ans