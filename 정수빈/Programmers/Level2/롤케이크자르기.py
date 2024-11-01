# https://school.programmers.co.kr/learn/courses/30/lessons/132265
# 설명
# 1. 형의 딕셔너리 old 만든다.
# 2. 동생의 딕셔너리 young을 만든다. (모든 토핑의 개수를 세서 넣는다.)
# 3. 토핑을 하나씩 살펴볼 때, old에 추가하고, young에 있는 경우 하나 뺀다.

# 단순하게 old와 young을 리스트로 만들어서 풀 수도 있지만, 딕셔너리로 만들어서 풀어야 시간초과가 나지 않는다. 

import collections

def solution(topping):
    answer = 0
    old = {}
    young = dict(collections.Counter(topping))
    for c in topping:
        if c in old:
            old[c] +=1
        else:
            old[c] = 1
        
        if c in young:
            if young[c] > 0:
                young[c] -= 1
                if young[c] == 0:
                    del young[c]
        if len(old) == len(young):
            answer +=1
    return answer