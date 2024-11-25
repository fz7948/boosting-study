# https://school.programmers.co.kr/learn/courses/30/lessons/43165
# 설명: bfs 문제지만 백트레킹으로 품
# 시간: 13분

def solution(numbers, target):   
    
    def bk(idx, num_sum, answer):
        if idx == len(numbers):
            if num_sum == target:
                answer += 1
            return answer

        a = bk(idx+1, num_sum + numbers[idx], answer)
        b = bk(idx+1, num_sum - numbers[idx], answer)
        
        return a + b
    
    return bk(0, 0, 0)