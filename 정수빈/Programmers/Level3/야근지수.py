# https://school.programmers.co.kr/learn/courses/30/lessons/12927#
# 설명: works의 원소들을 n만큼 줄여나가며 제곱한 값의 합을 구합니다.
# 파이썬의 힙큐는 최소큐만 하기때문에 -를 주고 최대 큐를 만든다

import heapq

def solution(n, works):
    if sum(works) - n < 0 :
        return 0
    
    max_heap = []
    for item in works:
        heapq.heappush(max_heap, -item)

    while n > 0:
        t = heapq.heappop(max_heap)
        heapq.heappush(max_heap, t + 1)
        n -= 1

    return  sum([w ** 2 for w in max_heap])