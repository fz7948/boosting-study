# https://school.programmers.co.kr/learn/courses/30/lessons/12980
# 설명: 문제는 복잡하지만 답은 간단하다. 숫자를 2진수로 변환한 후 1의 갯수를 세면 된다.

def solution(n):
    return str(format(n, "b")).count("1")