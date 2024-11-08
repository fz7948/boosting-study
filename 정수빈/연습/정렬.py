N = int(input())
nums = []
for i in range(N):
    nums.append(int(input()))


def quick_sort(nums, low, high):
    if len(nums) <= 1:
        return nums
    if low < high:
        pivot = partition(nums, low, high)
        quick_sort(nums, low, pivot-1)
        quick_sort(nums, pivot, high)
    return nums

def partition(nums, low, high):
    idx = low - 1
    pivot = nums[high]
    for i in range(low, high):
        if pivot > nums[i]:
            idx += 1
            nums[i], nums[idx] = nums[idx], nums[i]
    nums[idx+1], nums[high] = nums[high], nums[idx+1]
    return idx + 1

for i in quick_sort(nums, 0, len(nums)-1):
    print(i)