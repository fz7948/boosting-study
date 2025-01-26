class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        visited = set()
        m = len(matrix)
        n = len(matrix[0])
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0 and not (r, c) in visited:
                    visited.add((r, c))
                    for i in range(m):
                        if matrix[i][c] != 0:
                            matrix[i][c] = 0
                            visited.add((i, c))
                    for i in range(n):
                        if matrix[r][i] != 0:
                            matrix[r][i] = 0
                            visited.add((r, i))