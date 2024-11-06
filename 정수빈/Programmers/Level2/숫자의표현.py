# https://school.programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer = 0
    for i in range(1, 1+n):
        for j in range(i, 1+n):
            s = sum(range(i, j+1))
            if s > n:
                break
            elif s == n:
                answer +=1            
    return answer