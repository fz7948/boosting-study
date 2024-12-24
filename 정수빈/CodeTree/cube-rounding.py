n, m, r, c, k = list(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
instructions = list(map(int, input().split()))

class Cube:
    def __init__(self, bottom_num):
        self.top = 0
        self.bottom = bottom_num
        self.front = 0
        self.back = 0
        self.left = 0
        self.right = 0
    
    def rotateNorth(self, bottom_num):
        tmp = self.back
        self.back = self.top
        self.top = self.front 
        self.front = self.bottom
        if bottom_num == 0:
            self.bottom = tmp
        else:
            self.bottom = bottom_num
    
    def rotateSouth(self, bottom_num):
        tmp = self.front
        self.front = self.top
        self.top = self.back
        self.back = self.bottom
        if bottom_num == 0:
            self.bottom = tmp
        else:
            self.bottom = bottom_num
    
    def rotateWest(self, bottom_num):
        tmp = self.left
        self.left = self.top
        self.top = self.right
        self.right = self.bottom 
        if bottom_num == 0:
            self.bottom = tmp
        else:
            self.bottom = bottom_num

    def rotateEast(self, bottom_num):
        tmp = self.right
        self.right = self.top
        self.top = self.left
        self.left = self.bottom
        if bottom_num == 0:
            self.bottom = tmp
        else:
            self.bottom = bottom_num
    
    def print_top(self):
        print(self.top)

cube = Cube(grid[r][c])
# cube.print_top()
grid[r][c] = 0

# def print_grid():
#     for i in range(n):
#         print(grid[i])

for instruction in instructions:
    if instruction == 1:
        dr, dc = 0, 1
    elif instruction == 2:
        dr, dc = 0, -1
    elif instruction == 3:
        dr, dc = -1, 0
    elif instruction == 4:
        dr, dc = 1, 0
    nr, nc = r + dr, c + dc
    # print(nr, nc)
    if 0 <= nr < n and 0 <= nc < m:
        bottom_num = 0
        if grid[nr][nc] != 0:
            bottom_num = grid[nr][nc]
            # print(nr, nc)
            grid[nr][nc] = 0

        if instruction == 1:
            cube.rotateEast(bottom_num)
        elif instruction == 2:
            cube.rotateWest(bottom_num)
        elif instruction == 3:
            cube.rotateNorth(bottom_num)
        elif instruction == 4:
            cube.rotateSouth(bottom_num)
            
        if bottom_num == 0 and grid[nr][nc] == 0:
            grid[nr][nc] = cube.bottom

            
        cube.print_top()
        # print_grid()
        r, c = nr, nc