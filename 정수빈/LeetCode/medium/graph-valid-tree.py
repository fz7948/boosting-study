# https://leetcode.com/problems/graph-valid-tree/
# 걸린시간: 30분


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        from collections import deque
        if n > 0 and len(edges) < n-1:
            return False
        agj = [[0] * n for _ in range(n)]
        for a,b in edges:
            agj[a][b] = 1
            agj[b][a] = 1

        def dfs(head, q, visited):
            count = 1
            q.append(head)
            visited.add(head)
            while q:
                node = q.popleft()
                count += 1
                if node in q:
                    return False, None
                for i in range(n):
                    if i != head and agj[node][i] == 1 and not i in visited:
                        q.append(i)
                        visited.add(node)
            return True, count 
        ans = []
        visited = set()
        q = deque()
        for i in range(n):
            a, count = dfs(i,q, visited)
            ans.append(count)
            if a == False:
                return False
        if max(ans) < n:
            return False

        return True
        