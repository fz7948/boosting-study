# https://school.programmers.co.kr/learn/courses/30/lessons/43162
# 설명: dfs로 푸는 문제
# 해결 못함 ㅠ

def solution(n, computers):
    
    visited = [False for _ in range(n)]
    count = 0
    def dfs(v):
        visited[v] = True
        
        for neig in range(n):
            if not visited[neig] and computers[v][neig] == 1:
                dfs(neig)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            count +=1
    
    return count