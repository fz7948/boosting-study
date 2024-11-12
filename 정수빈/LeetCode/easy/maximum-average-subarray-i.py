# https://leetcode.com/problems/maximum-average-subarray-i
# 설명: 연속된 수의 합 중에 제일 큰 수를 구하는 문제입니다. 
# 4개의 요소의 합으로 구하는건 시간 초과 에러가 나서 우선 4개의 합을 구한다음에 이전요소는 빼고 다음요소는 더하는 방식으로 가야합니다. 


def findMaxAverage(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    if k == 1:
        return max(nums)

    tot = sum(nums[:k])
    maxN = sum(nums[:k]) /float(k)
    for i in range(1, len(nums)-k+1):
        tot = tot - nums[i-1] + nums[i+k-1]
        maxN = max(maxN, tot/ float(k)) 
    return maxN
print(findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4), 12.75000)
print(findMaxAverage(nums =[0,1,1,3,3], k = 4), 2.0)
print(findMaxAverage(nums=[4,2,1,3,3], k=2), 3)