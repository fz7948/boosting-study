def numberOfSubarrays(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    answer = 0
    nums = list(map(lambda x: x % 2, nums))
    for i in range(len(nums)):
        for j in range(i, len(nums)+1):
            if sum(nums[i:j]) == k:
                answer +=1
    return answer

print(numberOfSubarrays([1,1,2,1,1], 3), 2)
print(numberOfSubarrays([1,1,1,1,1],1), 5)
print(numberOfSubarrays([2,4,6],1), 0)
print(numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2), 16)