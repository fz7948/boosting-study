# https://school.programmers.co.kr/learn/courses/30/lessons/12914#
# 설명: 1과 2를 이용해 n을 만드는 경우의 수를 구합니다.
# 피보나치 수열과 동일한 방식으로 풀 수 있습니다.

def solution(n):
    fibo = [1, 2]
    for i in range(1, n-1):
        fibo.append(fibo[i]+fibo[i-1])
    return fibo[n-1] % 1234567