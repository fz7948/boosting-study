# https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float("inf")

        for i in range(len(nums)):
            lp, rp = i+1, len(nums)-1
            while lp < rp:
                total = nums[i] + nums[lp] + nums[rp]
                if abs(target-total) < abs(diff):
                    diff = target - total
                
                if total < target:
                    lp +=1
                else:
                    rp -= 1
            if diff == 0:
                break
        return target-diff