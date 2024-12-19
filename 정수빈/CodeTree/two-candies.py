# n, m = list(map(int, input().split()))
# board = [list(input()) for _ in range(n)]

# board = [
#     "######",
#     "#.##B#",
#     "##R..#",
#     "#..#.#",
#     "#O...#",
#     "######",
# ]
# board = [
#     "##########",
#     "#.O....RB#",
#     "##########",
# ]
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

def print_baord(board):
    for i in range(n):
        print(board[i])
    print()

def move(board, direction, red_r, red_c, blue_r, blue_c):
    if direction == "LEFT":
        dr, dc = 0, -1
        loop_count = m
    elif direction == "RIGHT":
        dr, dc = 0, 1
        loop_count = m
    elif direction == "DOWN":
        dr, dc = 1, 0
        loop_count = n
    else:
        dr, dc = -1, 0
        loop_count = n
    status = None
    for _ in range(loop_count):
        new_red_r, new_red_c = red_r + dr, red_c + dc
        new_blue_r, new_blue_c = blue_r + dr, blue_c + dc
        if 0 < new_red_c < m-1 and 0 < new_red_r < n-1 and status == None:
            if board[new_red_r][new_red_c] == ".":
                board[red_r][red_c] = "."
                board[new_red_r][new_red_c] = "R"
                red_r, red_c = new_red_r, new_red_c

            elif board[new_red_r][new_red_c] == "O":
                board[red_r][red_c] = "."
                red_r, red_c = new_red_r, new_red_c
                status = True
                
        if 0 < new_blue_c < m-1 and 0< new_blue_r < n-1:
            if board[new_blue_r][new_blue_c] == ".":
                board[blue_r][blue_c] = "."
                board[new_blue_r][new_blue_c] = "B"
                blue_r, blue_c = new_blue_r, new_blue_c

            elif board[new_blue_r][new_blue_c] == "O":
                blue_r, blue_c = new_blue_r, new_blue_c
                status = False
        if status == False:
            return red_r, red_c, blue_r, blue_c, status

    return red_r, red_c, blue_r, blue_c, status
    

## find red, blue coord
red_r, red_c = -1,-1
blue_r, blue_c = -1,-1
for r in range(n):
    for c in range(m):
        if board[r][c] == "R":
            red_r, red_c = r, c
        elif board[r][c] == "B":
            blue_r, blue_c = r, c

dir = ["LEFT", "RIGHT", "DOWN", "TOP"]
import copy
ans = 100
visited = set()
def dfs(count, board, direction, red_r, red_c, blue_r, blue_c):
    global ans
    if count == 11:
        return -1
    new_board = copy.deepcopy(board)
    red_r, red_c, blue_r, blue_c, status = move(new_board, direction, red_r, red_c, blue_r, blue_c)
    visited.add((red_r, red_c, blue_r, blue_c))
    if status == True:
        ans = min(ans, count)
        return
    elif status == False:
        return 
    
    for i in range(4):
        if direction != dir[i]:
            next_board = copy.deepcopy(new_board)
            dfs(count+1, next_board, dir[i], red_r, red_c, blue_r, blue_c)
    

for direction in dir:
    new_board = copy.deepcopy(board)
    dfs(1, new_board, direction, red_r, red_c, blue_r, blue_c)

if ans == 100:
    print(-1)
else:
    print(ans)