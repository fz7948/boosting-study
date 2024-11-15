class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        def col(board, x, y):
            return getNumbers([col[x] for col in board])
        
        def row(board, x, y):
            return getNumbers(board[y])
        
        def sq(board, x, y):
            if y in [0,1,2]:
                row1, row2, row3 = board[0], board[1], board[2]
            elif y in [3,4,5]:
                row1, row2, row3 = board[3],  board[4],  board[5]
            elif y in [6,7,8]:
                row1, row2, row3 = board[6], board[7], board[8]
            if x in [0,1,2]:
                tem = []
                tem.extend(row1[:3])
                tem.extend(row2[:3])
                tem.extend(row3[:3])
                return getNumbers(tem)
            elif x in [3,4,5]:
                tem = []
                tem.extend(row1[3:6])
                tem.extend(row2[3:6])
                tem.extend(row3[3:6])
                return getNumbers(tem)
            elif x in [6,7,8]:
                tem = []
                tem.extend(row1[6:9])
                tem.extend(row2[6:9])
                tem.extend(row3[6:9])
                return getNumbers(tem)
        
        def getNumbers(l):
            return list(filter(lambda x: x != ".", l))
            
        for y in range(len(board)):
            for x in range(len(board[0])):
                c = col(board, x, y)
                r = row(board, x, y)
                sqq = sq(board, x, y)
                if len(c) != len(set(c)) or len(r) != len(set(r))or len(sqq) != len(set(sqq)):
                    return False
        return True

print(Solution().isValidSudoku(board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))