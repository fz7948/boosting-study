# 문제: 올바른 괄호
# 괄호가 올바르게 닫혔는지 확인하는 문제
# 여는 괄호가 나오면 스택에 넣고, 닫는 괄호가 나오면 스택에서 꺼내서 짝이 맞는지 확인한다.
# 닫는 괄효가 나오면 스택에 있는 여는 괄호가 있는지 체크
# 닫는 괄호가 나오면 스택이 비어있으면 False를 반환한다.

def solution(s):
    answer = True
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")" and len(stack) > 0 and stack[-1] == "(":
            stack.pop(-1)
        elif c == ")" and len(stack) == 0:
            return False
    return len(stack) == 0