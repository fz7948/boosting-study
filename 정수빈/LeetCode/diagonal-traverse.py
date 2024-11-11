import math

def findDiagonalOrder(mat):
    left = 0
    right = 1
    top = 0
    bottom = 1
    answer = []
    upright = True
    new_mat = []
    if len(mat) == len(mat[0]):
        new_mat = mat.copy()
    else:
        sq_len = max(len(mat), len(mat[0]))
        for i in range(sq_len):
            new_mat.append([])
            for j in range(sq_len):
                new_mat[i].append(999999)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                new_mat[i][j] = mat[i][j]

    while left < len(new_mat):
        for i in range(right-left):
            if upright:
                if new_mat[bottom-i-1][left+i] != 999999:
                    answer.append(new_mat[bottom-i-1][left+i])
            else:
                if new_mat[top+i][right-1-i] != 999999:
                    answer.append(new_mat[top+i][right-1-i])
        upright = not upright
        
        if right < len(new_mat) and bottom < len(new_mat):
            right += 1
            bottom += 1
        elif right == len(new_mat) and bottom == len(new_mat):
            top += 1
            left += 1
    return answer

print(findDiagonalOrder(mat = [[1,2,3],[4,5,6],[7,8,9]]), [1,2,4,7,5,3,6,8,9])
print(findDiagonalOrder(mat = [[1,2,3]]), [1,2,3])