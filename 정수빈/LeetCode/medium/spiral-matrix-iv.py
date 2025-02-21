# https://leetcode.com/problems/spiral-matrix-iv/
# 걸린 시간: 10분

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:

        offset = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        grid = [[-1] * n for _ in range(m)]
        visited = set()
        node = head
        r, c, di = 0, 0, 0
        visited.add((r,c))
        grid[r][c] = node.val
        node = node.next
        dr, dc = offset[di]
        for i in range(n*m):
            if node == None:
                break
            nr, nc = r + dr, c + dc
            if 0<= nr < m and 0<= nc < n and (nr, nc) not in visited:
                visited.add((nr, nc))
                grid[nr][nc] = node.val
                r, c = nr, nc
            else:
                di += 1
                di %= 4
                dr, dc = offset[di]
                nr, nc = r + dr, c + dc
                if 0<= nr < m and 0<= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    grid[nr][nc] = node.val
                    r, c = nr, nc
            node = node.next
        return grid
