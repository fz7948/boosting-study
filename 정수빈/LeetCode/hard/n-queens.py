class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        grid = [["." for _ in range(n)] for _ in range(n)]
        ans = []
        if n == 1:
            return [["Q"]]
        
        def valid(qr, qc):
            for i in range(n):
                if grid[qr][i] == "Q":
                    return False
                if grid[i][qc] == "Q":
                    return False
                if 0<= qr+i< n and 0 <= qc+i < n and grid[qr+i][qc+i] == "Q":
                    return False
                if 0<= qr-i< n and 0 <= qc-i < n and grid[qr-i][qc-i] == "Q":
                    return False
                if 0<= qr+i< n and 0 <= qc-i < n and grid[qr+i][qc-i] == "Q":
                    return False
                if 0<= qr-i< n and 0 <= qc+i < n and grid[qr-i][qc+i] == "Q":
                    return False
            return True

        def bk(idx, count):

            if count == n:
                answer = []
                for i in range(n):
                    answer.append("".join(grid[i]))
                if not answer in ans:
                    ans.append(answer)
                return 
            
            if idx < n:
                for i in range(n):
                    if valid(idx, i):
                        grid[idx][i] = "Q"
                        bk(idx+1, count+1)
                        grid[idx][i] = "."
        
        bk(0, 0)
        return ans