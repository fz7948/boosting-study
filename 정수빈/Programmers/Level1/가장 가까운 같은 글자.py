# https://school.programmers.co.kr/learn/courses/30/lessons/142086
# 설명: 딕셔너리에 인덱스를 추가하여 해당 문자가 나온 인덱스를 저장하고, 그 차이를 계산하여 반환한다.

def solution(s):
    answer = []
    dict = {}
    
    for i in range(len(s)):
        if not s[i] in dict:
            dict[s[i]] = [i]
            answer.append(-1)
        else:
            l = dict[s[i]]
            answer.append(i-l[-1])
            dict[s[i]] = dict[s[i]] + [i]
    return answer