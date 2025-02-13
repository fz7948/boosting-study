# https://school.programmers.co.kr/learn/courses/30/lessons/17679?language=python3

def solution(m, n, board):
    answer = 0
    directions = [(0,0), (1,0), (0,1), (1,1)]
    board = [list(x) for x in board]
    def drop():
        for c in range(n):
            for r in range(m-1, -1, -1):
                if board[r][c] == None:
                    i = r-1
                    while i >= 0:
                        if board[i][c] != None:
                            board[r][c], board[i][c] = board[i][c], board[r][c]
                            break
                        i-=1
    
    def disappear():
        diss = set()
        for r in range(m):
            for c in range(n):
                character = board[r][c]
                four = []
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<m and 0<=nc<n and board[nr][nc] == character:
                        four.append((nr, nc))
                    else:
                        break
                if len(four) == 4:
                    for f in four:
                        diss.add(tuple(f))
        # print(diss)
        for r, c in diss:
            board[r][c] = None

    def count_disappear():
        count = 0
        for r in range(m):
            for c in range(n):
                if board[r][c] == None:
                    count += 1
        return count
    

    prev_count = None
    count = 0
    while prev_count != count:
        disappear()
        drop()
        prev_count = count
        count = count_disappear()
    return count