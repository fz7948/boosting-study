# https://school.programmers.co.kr/learn/courses/30/lessons/12945
# 설명: 리스트를 이용해 피보나치 수를 구합니다. 

def solution(n):
    fibo = [0, 1, 1]
    for i in range(2, n):
        fibo.append(fibo[i]+fibo[i-1])
    
    return fibo[-1] % 1234567