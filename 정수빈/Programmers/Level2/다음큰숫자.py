# https://school.programmers.co.kr/learn/courses/30/lessons/12911
# 2진수로 표현했을 때 1의 개수가 같은 숫자를 구하는 문제입니다. 
# 2진수로 변환한 후 1의 개수를 세어주었습니다.

def solution(n):
    answer = 0
    one = str(format(n, "b")).count("1")
    n2 = n+1
    while True:
        other = str(format(n2, "b")).count("1")
        if other == one:
            answer = n2
            break
        n2 += 1
    return answer