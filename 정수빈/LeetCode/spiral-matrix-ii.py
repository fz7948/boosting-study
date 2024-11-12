# https://leetcode.com/problems/spiral-matrix-ii/
# 설명: 나선모양으로 숫자를 배치한 후 2차원 배열을 출력
# 방문을 기록하기 위한 배열과 0으로 채워진 n*n 배열을 만듭니다. 
# 방문한 노드를 체크하기 위해 visited를 생성 
# offset 으로 미리 움직일 -1, 1을 정함, offset이 나선 움직임에 핵심

class Solution(object):
    def generateMatrix(self, n):
        offset = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        offidx = 0
        board = []
        visited = []
        for i in range(n):
            board.append([])
            for _ in range(n):
                board[i].append(0)
        for i in range(n):
            visited.append([])
            for _ in range(n):
                visited[i].append(False)
        
        count = 1
        y = 0
        x = 0
        while True:
            visited[y][x] = True
            board[y][x] = count
            xoff, yoff = offset[offidx]
            if y+ yoff <n and x + xoff < n and visited[y+ yoff][x + xoff] == False :
                x = x + xoff
                y = y+ yoff
                count += 1
            else:
                offidx += 1
                if offidx > 3:
                    offidx = 0
                if count == n * n:
                    break

        return board