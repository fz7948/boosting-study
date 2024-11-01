# https://school.programmers.co.kr/learn/courses/30/lessons/138476
# 설명
# 1. tangerine의 각 요소의 개수를 센다.
# 2. 개수가 많은 순으로 뽑아서 k를 뺀다.
# 3. k가 0이하가 되면 종료한다.

from collections import Counter

def solution(k, tangerine):
    answer = 0
    for _, count in Counter(tangerine).most_common():
        answer += 1
        k -= count
        if k <= 0:
            break
    return answer