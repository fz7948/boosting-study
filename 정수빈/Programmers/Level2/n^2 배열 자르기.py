# https://school.programmers.co.kr/learn/courses/30/lessons/87390
# n*n 배열을 자르는 문제이다. n*n 배열을 1부터 n*n까지 i로 채우고, 1차원 배열로 만들어서 left와 right 사이의 값을 반환하는 문제이다.
# 1차원으로 변환하면 좌표를 통해 계산할 수 있다.
# 칸의 값은 max(i // n+1, i % n+1)로 나타낼 수 있다.

def solution(n, left, right):
    l = []
    for i in range(left, right+1):
        l.append(max(i // n+1, i % n+1))
    return l