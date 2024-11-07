# https://school.programmers.co.kr/learn/courses/30/lessons/12981
# 설명: 같은 단어를 다시 말하거나, 끝말잇기가 틀렸을 때 몇번째 사람이 몇번째 차례에 틀렸는지 반환하는 문제
# 풀이: 단어를 저장할 딕셔너리를 만들고, 단어를 하나씩 검사하면서 딕셔너리에 없는 단어인 경우 딕셔너리에 추가하고, 이미 있는 단어인 경우 해당 단어가 몇번째 차례에 나왔는지 반환한다.


def solution(n, words):
    answer = []
    dict = {}
    dict[words[0]]=1
    for i in range(1, len(words)):
        word = words[i]
        if words[i] not in dict:
            dict[word] = 1
        else:
            answer = [i%n+1, i//n+1]
            break
        if not words[i-1][-1] == words[i][0]:
            answer = [i%n+1, i//n+1]
            break
        
    if answer == []:
        answer= [0,0]
    return answer