# https://school.programmers.co.kr/learn/courses/30/lessons/76502
# 설명: 문자열을 회전시키면서 올바른 괄호 문자열인지 확인하는 문제입니다.
# 가장 바깥에 문자열을 회전하는 loop
# stack을 사용하여 올바른 괄호 확인

def solution(s):
    answer = 0
    rotated = s
    stack = []
    for i in range(len(s)):
        rotated = s[i:]+s[:i]
        for c in rotated:
            only_closed = False
            if c == "{" or c == "(" or c == "[":
                stack.append(c)
            elif len(stack) <= 0:
                only_closed = True
                continue
            elif stack[-1] == "{" and c == "}":
                stack.pop(-1)
            elif stack[-1] == "(" and c == ")":
                stack.pop(-1)
            elif stack[-1] == "[" and c == "]":
                stack.pop(-1)
            else:
                continue
        if len(stack) == 0 and not only_closed:
            answer += 1
        only_closed = False
        stack = []
    return answer