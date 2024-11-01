# https://school.programmers.co.kr/learn/courses/30/lessons/70129
# 설명
# 1. 0을 제거한다.
# 2. 0을 제거한 문자열의 길이를 2진법으로 변환한다.
# 3. 이진변환 한 횟수와 지워진 0의 개수를 센다.

def solution(s):
    answer = []
    count = 0
    zero_count = 0
    while s != "1":
        reduce_s = s.replace("0", "")
        y_s = format(len(reduce_s), 'b')
        zero_count += len(s) - len(reduce_s)
        count += 1
        s = y_s
    return [count, zero_count]