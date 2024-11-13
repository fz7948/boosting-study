def solution(foods):
    total_sum = sum(foods)
    
    # 전체 합이 3으로 나누어지지 않으면 세 등분 불가
    if total_sum % 3 != 0:
        return 0

    target_sum = total_sum // 3
    current_sum = 0
    first_split_count = 0
    result = 0
    
    # 두 번째 분할 지점부터 세 번째 분할 지점까지 탐색
    for i in range(len(foods) - 1):
        current_sum += foods[i]
        
        # 두 번째 구간을 찾았을 때, 첫 번째 구간의 개수를 추가
        if current_sum == 2 * target_sum and i < len(foods) - 1:
            result += first_split_count
        
        # 첫 번째 구간이 타겟 포만도일 때 카운트 증가
        if current_sum == target_sum:
            first_split_count += 1

    return result

            

print(solution([1,2,3,0,3]), 2)
print(solution([1,2,3,0,0,3]), 2)
print(solution([2, 1, 1, 2]), 1)
print(solution([4, 1]), 0)
print(solution([0, 0, 0]), 0)