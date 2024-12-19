from collections import deque

board = [
    "##########",
    "#.#...#..#",
    "#R..#....#",
    "#######.##",
    "#....#..##",
    "#.####O#B#",
    "#.#......#",
    "#........#",
    "#....#...#",
    "##########",
]

n, m = len(board), len(board[0])

for i in range(n):
    board[i] = list(board[i])

# 방향 설정 (왼, 오, 위, 아래)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 초기 위치 찾기
red_r, red_c, blue_r, blue_c = -1, -1, -1, -1
for r in range(n):
    for c in range(m):
        if board[r][c] == "R":
            red_r, red_c = r, c
        elif board[r][c] == "B":
            blue_r, blue_c = r, c

# BFS 탐색
def move(r, c, dr, dc):
    steps = 0
    # 다음 칸이 벽이거나 구멍이 될 때까지 이동
    while board[r + dr][c + dc] != '#' and board[r][c] != 'O':
        r += dr
        c += dc
        steps += 1
    return r, c, steps

def bfs():
    queue = deque([(red_r, red_c, blue_r, blue_c, 0)])
    visited = set()
    visited.add((red_r, red_c, blue_r, blue_c))

    while queue:
        rr, rc, br, bc, count = queue.popleft()
        
        # 10번 초과 시 실패
        if count >= 10:
            continue
        
        for dr, dc in directions:
            # 빨간 구슬 이동
            nrr, nrc, r_steps = move(rr, rc, dr, dc)
            # 파란 구슬 이동
            nbr, nbc, b_steps = move(br, bc, dr, dc)

            # 파란 구슬이 구멍에 빠지면 실패
            if board[nbr][nbc] == 'O':
                continue

            # 빨간 구슬만 구멍에 빠지면 성공
            if board[nrr][nrc] == 'O':
                return count + 1

            # 두 구슬이 겹쳤다면, 이동 거리가 더 짧은 구슬을 한 칸 뒤로
            if (nrr, nrc) == (nbr, nbc):
                if r_steps > b_steps:
                    nrr -= dr
                    nrc -= dc
                else:
                    nbr -= dr
                    nbc -= dc

            # 새로운 상태를 큐에 추가
            if (nrr, nrc, nbr, nbc) not in visited:
                visited.add((nrr, nrc, nbr, nbc))
                queue.append((nrr, nrc, nbr, nbc, count + 1))
    
    return -1

# 결과 출력
print(bfs())
