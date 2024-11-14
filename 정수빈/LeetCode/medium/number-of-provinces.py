# https://leetcode.com/problems/number-of-provinces
# 설명: dfs 문제입니다. 아 진짜 너무 어렵네여 

class Solution(object):
    def findCircleNum(self, isConnected):
        def dfs(i):
            visited[i] = True
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and not visited[j]:
                    dfs(j)
        
        provinces = 0
        visited = [False] * len(isConnected)

        for i in range(len(isConnected)):
            if not visited[i]:
                provinces += 1
                dfs(i)

        return provinces
