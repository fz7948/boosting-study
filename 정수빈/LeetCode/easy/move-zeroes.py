def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    if len(nums) == 1:
        return nums
    
    idx = 0
    count = 0
    while count < len(nums):
        if nums[idx] == 0:
            nums.pop(idx)
            nums.append(0)
        else:
            idx += 1
        count += 1
    return nums
print(moveZeroes(nums = [0,1,0,3,12]), [1,3,12,0,0])