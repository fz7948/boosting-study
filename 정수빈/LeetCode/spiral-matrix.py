# https://leetcode.com/problems/spiral-matrix/
# 설명: 2차원 배열을 소용돌이 모양으로 출력
# 방문한 노드를 체크하기 위해 visited를 생성 
# offset 으로 미리 움직일 -1, 1을 정함, offset이 소용돌이 움직임에 핵심

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        visited = []
        for _ in range(len(matrix)):
            s = []
            for _ in range(len(matrix[0])):
                s.append(False)
            visited.append(s)
    
        row_len = len(matrix[0])
        col_len = len(matrix)
        offset = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        i = 0
        j = 0
        answer = []
        offidx = 0
        while True:
            xoff, yoff = offset[offidx]
            if not visited[i][j]:
                visited[i][j] = True
                answer.append(matrix[i][j])
            if i + yoff < col_len and j + xoff < row_len and not visited[i + yoff][j + xoff]:
                i = i + yoff
                j = j + xoff
            else:
                offidx += 1
                if offidx > 3:
                    offidx = 0
            if len(answer) == row_len * col_len:
                break
        return answer
        