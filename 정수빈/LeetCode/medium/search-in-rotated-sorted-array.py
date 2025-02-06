# https://leetcode.com/problems/search-in-rotated-sorted-array/
# 걸린시간: 40분 결국 답지봄
# 뭔가 한번에 구하는 방법이 있을줄 알았는데, 간단하게 피봇을 구하고 두번 이진탐색하는 방법이 있었다.. 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) - 1
        # find pivot
        pivot = nums[0]
        while lp <= rp:
            mid =(lp + rp)// 2
            if nums[mid] > nums[-1]:
                lp = mid + 1
            else:
                rp = mid -1
            
        def binarySearch(left_boundary, right_boundary):
            lp, rp = left_boundary, right_boundary
            while lp <= rp:
                mid = (lp + rp) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    rp = mid - 1
                else:
                    lp = mid + 1
            return -1
        
        ans = binarySearch(0, lp-1)
        if  ans != -1:
            return ans
        return binarySearch(lp, len(nums) -1)
