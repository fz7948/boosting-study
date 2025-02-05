class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(n):
            prev = matrix[0][i]
            for j in range(n):
                if j < m and j+i < n and prev != matrix[j][i+j]:
                    return False
                else:
                    pass

        for i in range(m):
            prev = matrix[i][0]
            for j in range(m):
                if j < n and j+i < m and prev != matrix[i+j][j]:
                    return False
                else:
                    pass
                
        return True